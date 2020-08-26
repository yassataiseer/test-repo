from flask import Flask, render_template,request,session
import json
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from test import data_answer
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db= SQLAlchemy(app)






class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.Text)
    Password = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Server = db.Column(db.Text)
    Timing = db.Column(db.Text)
    About = db.Column(db.Text)
    Name = db.Column(db.Text)
    Profile_pic = db.Column(db.LargeBinary)
    db.create_all()


@app.route("/")
def index():
    return render_template("sign-up.html")


@app.route("/signup")
def register_user():
    return render_template("sign-up.html", )

@app.route("/players")
def view_players():
    data = data_answer.data()
    return render_template("profiles.html",data=data)

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/upload")
def load():
    return render_template("index.html", )


global email_id
email_id = None

@app.route("/profile")
def profile():
    global email_id 
    print("EMAIL ID ", email_id)
    user = User.query.filter_by(Email=email_id).first()
    print(user)
    bday = user.Age
    server = user.Server
    time = user.Timing
    about = user.About
    name = user.Name
    db.create_all()
    db.session.add(user)
    db.session.commit()

    return render_template("index.html", email=email_id,bday=bday,time=time,server=server,about=about,name=name)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/logger", methods = ['POST'])
def log():
    email = request.form['emailer']
    password = request.form['pswrd']
    user = User(Email=email, Password=password,Age=None, Server = None, Timing = None, About = None, Name=None, Profile_pic=None)
    print("logger")
    existing_user = User.query.filter_by(Email=email).first()
    pasword_checker = User.query.filter_by(Password=password).first()
    print(existing_user)
    print(pasword_checker)
    if existing_user is None or pasword_checker is None:
        return 'invalid creds'
    else:
        global email_id
        email_id = email
        print("EMAIL ID", email_id)
        return render_template("home.html")  
        

    



@app.route("/sign", methods = ['POST'])
def register():
    print("hello there")
    email = request.form['email']
    password = request.form['psw']
    repeat = request.form['psw-repeat']
    user = User(Email=email, Password=password)
    print(user)
    existing_user = User.query.filter_by(Email=email).first()
    if password != repeat or existing_user is not None:
        return 'invalid credentials the email used may have already been in use or your repeat and original passswords are different '
    elif password==repeat:
        db.create_all()
        db.session.add(user)
        db.session.commit()
        global email_id 
        email_id = email
        print("email", email_id)
        return render_template("home.html",email=email) 



@app.route("/data", methods = ['POST'])
def data():
    print("hello there")
    email = request.form['email']
    password = request.form['psw']
    repeat = request.form['psw-repeat']
    user = User(Email=email, Password=password)
    print(user)
    existing_user = User.query.filter_by(Email=email).first()
    if password != repeat or existing_user is not None:
        return 'invalid credentials the email used may have already been in use or your repeat and original passswords are different '
    elif password==repeat:
        db.create_all()
        db.session.add(user)
        db.session.commit()

        return render_template("home.html",Email_org=email) 


@app.route("/collect", methods = ['POST'])
def collector():
    print("collecter")
    email = request.form['email']
    bday = request.form['bdate']
    time = request.form['time']
    server = request.form['servers']
    about = request.form['about']
    name = request.form['name']
    user = User.query.filter_by(Email=email).first()
    user.Age = bday
    user.Server = server
    user.Timing = time
    user.About = about
    user.Name=name
    db.create_all()
    db.session.add(user)
    db.session.commit()
    global email_id 
    email_id = email
    print("email44", email_id)
    return render_template("index.html", email=email,bday=bday,time=time,server=server,about=about,name=name)



if __name__ == '__main__':
    app.run(debug=True)
