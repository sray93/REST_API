# REST_API

Requirements: <br>
• Create, Update, Delete, List web service endpoints for a User object. <br>
• User object should contain a name, email address, password and the date of their last login. <br>
• Provide a login endpoint that validates the email address and password provided by the user matches the one stored in the database. <br>

Technologies user: <br>
Flask, Python, MySQL <br>

How to Run: <br>
Download Source_code folder to your system. <br>
Setup flask on your system. <br>
Install packages from requirements.txt <br>
For linux: <br>
  $ export FLASK_APP=app.py <br>
  $ flask run <br>

The flask inbuilt server runs on localhost. <br>

APIs endpoints provided: <br>
1. http://127.0.0.1:5000/listusers  : Get list of all users <br>
2. http://127.0.0.1:5000/createuser : Create new user <br>
3. http://127.0.0.1:5000/updateuser/<email> : Update user <br>
4. http://127.0.0.1:5000/deleteuser/<email> : Delete user <br>
5. http://127.0.0.1:5000/userlogin/<email> : Login endpoint <br>

