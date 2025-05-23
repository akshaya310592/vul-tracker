from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from typing import List
from uuid import uuid4
from app.models import Application, ApplicationCreate, DependencyInfo, DependencyDetails
from app import storage
from app.parser import parse_requirements
from app.osv_client import get_vulnerabilities

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/applications", response_model=Application)
async def create_application(
    name: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...)
):
    content = (await file.read()).decode()
    deps_raw = parse_requirements(content)

    app_id = str(uuid4())
    dependencies = []

    for pkg, version in deps_raw:
        vulns = get_vulnerabilities(pkg, version)
        dep_key = f"{pkg}=={version}"
        dependencies.append(DependencyInfo(name=pkg, version=version, vulnerabilities=vulns))

        # Update global dependency store
        if dep_key not in storage.dependencies:
            storage.dependencies[dep_key] = {
                "name": pkg,
                "version": version,
                "used_in": [app_id],
                "vulnerabilities": vulns
            }
        else:
            storage.dependencies[dep_key]["used_in"].append(app_id)

    app_obj = Application(
        id=app_id,
        name=name,
        description=description,
        dependencies=dependencies
    )

    storage.applications[app_id] = app_obj
    return app_obj

@app.get("/applications", response_model=List[Application])
def list_applications():
    return list(storage.applications.values())

@app.get("/applications/{app_id}/dependencies", response_model=List[DependencyInfo])
def get_app_dependencies(app_id: str):
    app_obj = storage.applications.get(app_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_obj.dependencies

@app.get("/dependencies", response_model=List[DependencyDetails])
def list_dependencies():
    return list(storage.dependencies.values())
