# EmployeeDirectory

A Django-based project that provides RESTful APIs to manage employees and departments within a company.

This application is designed to handle CRUD operations efficiently and ensure robust management of organizational data.


### Use Cases:

- Organize employee records in small to medium-sized companies.
- Manage departmental data and associations.
- Simplify backend integration for HR management systems.


### Tech Stack
- Backend: Django, Django REST Framework
- Database: SQLite (default, can be replaced)
- Environment Management: Virtualenv

### Requirements
- Python 3.8+
- pip 20.0+
- virtualenv 16.0+
- SQLite (default) or PostgreSQL/MySQL for production


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

##### GET /directory/employees
- **Description**: Retrieves a list of all employees in the company.
- **Response**: 
    - `200 OK`: Returns an array of employee objects.

##### POST /directory/employees
- **Description**: Creates a new employee.
- **Request Body**:
    - json object of employee data
- **Response**: 
    - `201 Created`: Returns the created employee object.
    - `400 Bad Request`: If the request body is invalid.

##### GET /directory/employees/{pk}
- **Description**: Retrieves a specific employee by its pk.
- **Path Parameters**:
    - `pk` (int): The primary key field of an employee.
- **Response**: 
    - `200 OK`: Returns the employee object.
    - `404 Not Found`: If the employee with the specified pk does not exist.

##### PUT /directory/employee/{pk}
- **Description**: Updates an existing employee by its pk.
- **Path Parameters**:
    - `pk` (int): The unique identifier of the employee.
- **Request Body**:
    - json object of employee data
- **Response**: 
    - `200 OK`: Returns the updated employee object.
    - `400 Bad Request`: If the request body is invalid.
    - `404 Not Found`: If the employee with the specified pk does not exist.

##### DELETE /directory/employee/{pk}
- **Description**: Deletes a specific employee by its pk.
- **Path Parameters**:
    - `pk` (int): The unique identifier of the employee.
- **Response**: 
    - `204 No Content`: If the employee was successfully deleted.
    - `404 Not Found`: If the employee with the specified pk does not exist.


#### Departments

##### GET /directory/departments
- **Description**: Retrieves a list of all departments in the company.
- **Response**: 
    - `200 OK`: Returns an array of department objects.

##### POST /directory/departments
- **Description**: Creates a new department.
- **Request Body**:
  - json object of department data
- **Response**: 
  - `201 Created`: Returns the created department object.
  - `400 Bad Request`: If the request body is invalid.


##### GET /directory/departments/{pk}
- **Description**: Retrieves a specific department by its pk.
- **Path Parameters**:
    - `pk` (int): The primary key field of a department.
- **Response**: 
    - `200 OK`: Returns the department object.
    - `404 Not Found`: If the department with the specified pk does not exist.

##### PUT /directory/departments/{pk}
- **Description**: Updates an existing department by its pk.
- **Path Parameters**:
  - `pk` (int): The unique identifier of the department.
- **Request Body**:
  - json object of department data
- **Response**: 
  - `200 OK`: Returns the updated department object.
  - `400 Bad Request`: If the request body is invalid.
  - `404 Not Found`: If the department with the specified pk does not exist.

##### DELETE /directory/departments/{pk}
- **Description**: Deletes a specific department by its pk.
- **Path Parameters**:
  - `pk` (int): The unique identifier of the department.
- **Response**: 
  - `204 No Content`: If the department was successfully deleted.
  - `404 Not Found`: If the department with the specified pk does not exist.


##### GET /directory/departments/{pk}/employees
- **Description**: Retrieves a list of all employees at a specific department in the company by the department pk.
- **Path Parameters**:
    - `pk` (int): The primary key field of a department.
- **Response**: 
    - `200 OK`: Returns an array of employee objects.

##### POST /directory/departments/{pk}/employees
- **Description**: Creates a new employee in a specific department.
- **Path Parameters**:
  - `pk` (int): The primary key field of a department.
- **Request Body**:
  - json object of employee data
- **Response**: 
  - `201 Created`: Returns the created employee object.
  - `400 Bad Request`: If the request body is invalid.


##### GET /directory/departments/{pk}/employees/{emp_pk}
- **Description**: Retrieves a specific employee at a specific department in the company by the department pk and the employee pk.
- **Path Parameters**:
    - `pk` (int): The primary key field of a department.
    - `emp_pk` (int): The primary key field of an employee.
- **Response**: 
    - `200 OK`: Returns the employee object.
    - `404 Not Found`: If the employee with the specified emp_pk does not exist in the department with the specified pk.

##### PUT /directory/departments/{pk}/employees/{emp_pk}
- **Description**: Updates an existing employee at specific department by its pk.
- **Path Parameters**:
  - `pk` (int): The unique identifier of the department.
  - `emp_pk` (int): The primary key field of an employee.
- **Request Body**:
  - json object of employee data
- **Response**: 
  - `200 OK`: Returns the updated employee object.
  - `400 Bad Request`: If the request body is invalid.
  - `404 Not Found`: If the employee with the specified emp_pk does not exist.

##### DELETE /directory/departments/{pk}
- **Description**: Deletes a specific department by its pk.
- **Path Parameters**:
  - `pk` (int): The unique identifier of the department.
- **Response**: 
  - `204 No Content`: If the department was successfully deleted.
  - `404 Not Found`: If the department with the specified pk does not exist.