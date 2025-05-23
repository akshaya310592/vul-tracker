# 🛡️ Vul-Tracker: Python Dependency Vulnerability Tracker

**Objective:**  
Develop a Python application using **FastAPI** that allows users to track vulnerabilities in their Python applications' dependencies. This project serves as a demonstration of backend development skills, RESTful API design, and performance optimization.

## 🚀 Features

### User Story
> As a Python developer, I want to track vulnerabilities in my application's dependencies to ensure its security and reliability.

### Functional Requirements

#### 📦 Application Endpoints

- **POST `/applications/`**  
  Create a new application by submitting:
  - `name` (string)
  - `description` (optional string)
  - `requirements.txt` file (uploaded)

- **GET `/applications/`**  
  List all applications with an indicator for vulnerable ones.

- **GET `/applications/{app_id}/dependencies/`**  
  Retrieve a specific application’s dependencies, and highlight those with known vulnerabilities.

#### 🧩 Dependency Endpoints

- **GET `/dependencies/`**  
  List all dependencies tracked across all applications and flag any that are vulnerable.

- **GET `/dependencies/{package_name}/`**  
  Get detailed information about a specific dependency:
  - Applications that use it
  - Vulnerabilities associated with it

---

## 🧰 Tech Stack

- **Python 3.10+**
- **FastAPI** – for building the REST API
- **httpx / requests** – for communicating with the [OSV.dev API](https://osv.dev)
- **pydantic** – for data validation
- **uvicorn** – ASGI server for running FastAPI
- **In-memory data store** – to manage application and dependency data (can be extended with Redis or a database)

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/vul-tracker.git
   cd vul-tracker
   
## Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Run the FAST API
uvicorn main:app --reload

## Project Structure
vul-tracker/
├── main.py                 # FastAPI application entry point
├── models.py               # Pydantic models
├── services/               # Business logic (e.g., OSV API integration)
├── storage.py              # In-memory data management
├── requirements.txt
└── README.md







   
