from app.models import Application, DependencyDetails

# In-memory database
applications: dict[str, Application] = {}
dependencies: dict[str, DependencyDetails] = {}

def reset_storage():
    applications.clear()
    dependencies.clear()
