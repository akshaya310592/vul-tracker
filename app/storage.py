from typing import Dict
from app.models import Application, DependencyDetails

# In-memory database
applications: Dict[str, Application] = {}
dependencies: Dict[str, DependencyDetails] = {}

def reset_storage():
    applications.clear()
    dependencies.clear()
