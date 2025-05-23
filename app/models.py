from pydantic import BaseModel

class DependencyInfo(BaseModel):
    name: str
    version: str
    vulnerabilities: list[dict] | None = []

class ApplicationCreate(BaseModel):
    name: str
    description: str

class Application(ApplicationCreate):
    id: str
    dependencies: list[DependencyInfo]

class DependencyDet
