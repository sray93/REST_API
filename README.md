# REST_API

Requirements:
• Create, Update, Delete, List web service endpoints for a User object.
• User object should contain a name, email address, password and the date of their last login.
• Provide a login endpoint that validates the email address and password provided by the user
matches the one stored in the database.

Technologies user:
Flask, Python, MySQL

How to Run:
Download Source_code folder to your system.
Setup flask on your system.
Install packages from requirements.txt
For linux:
  $ export FLASK_APP=app.py
  $ flask run

The flask inbuilt server runs on localhost.

APIs endpoints provided:
1. http://127.0.0.1:5000/listusers  : Get list of all users
2. http://127.0.0.1:5000/createuser : Create new user
3. http://127.0.0.1:5000/updateuser/<email> : Update user
4. http://127.0.0.1:5000/deleteuser/<email> : Delete user
5. http://127.0.0.1:5000/productslogin/<email> : Login endpoint

