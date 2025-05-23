Objective:
Develop a Python application using FastAPI that allows users to track vulnerabilities within their Python applications. This exercise is designed to evaluate your back-end development skills, API design, and optimization abilities.
 
User Story:
As a Python developer, I want to track vulnerabilities in my application's dependencies to ensure its security and reliability.
 
Functional Requirements:
           1. Application Endpoint:
           - Create application: Allow users to create a Python application by submitting a name, description, and requirements.txt file.
           - Get applications: List users’ applications. Identify vulnerable applications.
           - Get application dependencies: Retrieve the dependencies for a specified application and identify which of these dependencies are vulnerable.
 
           2.Dependency Endpoint:
           - Get dependencies: List all dependencies tracked across the user’s applications. Identify vulnerable dependencies.
           - Get dependency: Provide details about a specific dependency, including usage and associated vulnerabilities
