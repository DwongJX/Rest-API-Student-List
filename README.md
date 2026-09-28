# **Student List REST API**



A simple REST API built using Flask and SQLAlchemy for managing student records.



The API allows users to create, retrieve, update and delete student information using standard HTTP methods such as GET, POST, PUT and DELETE.



Student data is stored local using an SQLite database.



#### Features



* Retrieves all students
* Retrieve a specific student by ID
* Add new student
* Update existing student
* Delete a student



#### What was used



* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Postman



#### Structure Used in JSON



{

&#x20; "id": 1,

&#x20; "name": "Daryl",

&#x20; "school": "SIT",

&#x20; "gpa": 4.0

}



#### How it works



The Flask application creates a REST API that communicates with an SQLite database through SQLAlchemy.



When an HTTP request is sent to an API endpoint, Flask routes the request to the corresponding function.



The API follows basic CRUD operations:

CRUD operation			HTTP Method			Purpose

\------------------------------------------------------------------------------------------------------

Create				POST				Add new student

Read				GET				Retrieve student information

Update				PUT				Update an existing student

Delete				DELETE				Remove a student



1. ###### Run the Application

The default API should be: http://127.0.0.1:5000

###### 

###### 2\. Test the API Endpoints


Example 1: GET /


http://127.0.0.1:5000/



Result:

{

&#x20; "Message": "This is a Student List API"

}

------------------------------------------------------------------------------------------------------


Example 2: GET /students

http://127.0.0.1:5000/students

Result:
\[

&#x20; {

&#x20;   "id": 1,

&#x20;   "name": "Daryl",

&#x20;   "school": "SIT",

&#x20;   "gpa": 4.0

&#x20; },

&#x20; {

&#x20;   "id": 2,

&#x20;   "name": "John",

&#x20;   "school": "NUS",

&#x20;   "gpa": 3.8

&#x20; }

]

------------------------------------------------------------------------------------------------------

Example 3: GET /students/<student\_id>

http://127.0.0.1:5000/students/1

Result:
{

&#x20; "id": 1,

&#x20; "name": "Daryl",

&#x20; "school": "SIT",

&#x20; "gpa": 4.0

}

If student does not exist:
{

&#x20; "Error": "Student not found"

}

Status Code: 404 Not Found

------------------------------------------------------------------------------------------------------

Example 4: POST /students

http://127.0.0.1:5000/students

In Postman, select: Body → raw → JSON

Example request body:
{

&#x20; "name": "Daryl",

&#x20; "school": "SIT",

&#x20; "gpa": 4.0

}

Result:
{

&#x20; "id": 1,

&#x20; "name": "Daryl",

&#x20; "school": "SIT",

&#x20; "gpa": 4.0

}

Status Code: 201 Created

------------------------------------------------------------------------------------------------------

Example 5: PUT /students/<student\_id>

http://127.0.0.1:5000/students/1

Example Request:
{

&#x20; "name": "Daryl Wong",

&#x20; "gpa": 4.2

}

Result:
{

&#x20; "id": 1,

&#x20; "name": "Daryl Wong",

&#x20; "school": "SIT",

&#x20; "gpa": 4.5

}

If it does not exist:
Status Code: 404 Not Found


------------------------------------------------------------------------------------------------------



Example 6: DELETE /students/<student\_id>

http://127.0.0.1:5000/students/1

Result:
{

&#x20; "message": "Student has been successfully removed"

}

If student not found:
{

&#x20; "Error": "Student is not found"

}

------------------------------------------------------------------------------------------------------


Project Structure
---


Student-API/
---

###### │

###### ├── main.py

###### ├── instance/

###### │   └── studentlist.db

###### └── README.md





