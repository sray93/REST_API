from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from datetime import date
import re

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:sree@MSUS2020@localhost:3306/genesys'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    name = db.Column(db.String(500) )
    email = db.Column(db.String(500), primary_key=True )
    password = db.Column(db.String(500))
    lastlogin = db.Column(db.Date)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,name,email,password,lastlogin):
        self.name = name
        self.email = email
        self.password = password
        self.lastlogin = lastlogin
    def __repr__(self):   #returns string representation of the object
        return '' % self.name

class UserSchema(ModelSchema): #output format is defined by Marshmellow
    name = fields.String(dump_only=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    lastlogin = fields.Date(required=True)
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)

def check(email): 
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)): 
        return True
    else: 
        return False
   
#listing all users
@app.route('/listusers', methods = ['GET'])
def get_all_users():
    get_user = User.query.all()
    users = users_schema.dump(get_user)
    return make_response(jsonify({"users": users}))

#creating user
@app.route('/createuser', methods = ['POST'])
def create_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    #lastlogin = request.json['lastlogin']
    if User.query.get(email):
        return 'User already exists'
    if check(email) is False:
        return 'Please enter a valid email address'
    newUser = User(name,email,password,d1)
    db.session.add(newUser)
    db.session.commit()
    return 'User created successfully'
    
#updating user
@app.route('/updateuser/<email>', methods = ['PUT'])
def update_user(email):
    name = request.json['name']
    password = request.json['password']
    user = User.query.get(email)
    if user is None:
        return 'User does not exist'
    user.name = name
    user.password = password
    db.session.commit()
    return 'User updated successfully'

#deleting user
@app.route('/deleteuser/<email>', methods = ['DELETE'])
def delete_user(email):
    user = User.query.get(email)
    if user is None:
        return 'User does not exist'
    db.session.delete(user)
    db.session.commit()
    return 'User deleted successfully'

#login endpoint for user
@app.route('/userlogin/<email>', methods = ['POST'])
def login(email):
    password = request.json['password']
    user = User.query.get(email)
    if user is None:
        return 'User does not exist'
    if user.password == password:
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        user.lastlogin = d1
        db.session.commit()
        return 'Login successful'
    else:
        return 'Login unsuccessful. Please check username or password'
    

if __name__ == "__main__":
    app.run(debug=True)