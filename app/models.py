from pydantic import BaseModel
from typing import List, Optional

class DependencyInfo(BaseModel):
    name: str
    version: str
    vulnerabilities: Optional[List[dict]] = []

class ApplicationCreate(BaseModel):
    name: str
    description: str

class Application(ApplicationCreate):
    id: str
    dependencies: List[DependencyInfo]

class DependencyDetails(BaseModel):
    name: str
    version: str
    used_in: List[str]
    vulnerabilities: Optional[List[dict]] = []
