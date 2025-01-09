# EmployeeDirectory

A Django-based project that provides RESTful APIs to manage employees and departments within a company.

This application is designed to handle CRUD operations efficiently and ensure robust management of organizational data.

### Features
- Manage Employees: Create, read, update, and delete employee records.
- Manage Departments: Handle departmental information and assignments.
- User Authentication: Includes support for admin users via Django's built-in authentication system.
- Scalable and Modular: Built using Django REST Framework for extensibility and maintainability.

### Requirements
- Python 3.x
- pip
- virtualenv


### Setup Instructions
1. Clone the Repository
  Clone this repository to your local machine:
  ```bash
git clone <repository_url>
cd EmployeeDirectory

  ```

2. Set Up a Virtual Environment
  Create and activate a virtual environment:
  ```bash
virtualenv env
source env/bin/activate    # For macOS/Linux
source env/Scripts/activate  # For Windows
  ```

3. Install Dependencies
  Install the required Python packages:
  ```bash
pip install -r requirements.txt
  ```

4. Run Database Migrations
  Apply the migrations to set up the database:
  ```bash
python manage.py migrate
  ```


5. Create a Superuser
  Set up an admin account for the application:
  ```bash
python manage.py createsuperuser --email admin@example.com --username admin
  ```

6. Start the Development Server
  Run the Django development server:
  ```bash
python manage.py runserver
  ```

### API Endpoints
The following API endpoints are available:

#### Employees
- GET /api/employees/ - List all employees
- POST /api/employees/ - Create a new employee
- GET /api/employees/<id>/ - Retrieve a specific employee
- PUT /api/employees/<id>/ - Update an employee
- DELETE /api/employees/<id>/ - Delete an employee

#### Departments
- GET /api/departments/ - List all departments
- POST /api/departments/ - Create a new department
- GET /api/departments/<id>/ - Retrieve a specific department
- PUT /api/departments/<id>/ - Update a department
- DELETE /api/departments/<id>/ - Delete a department
