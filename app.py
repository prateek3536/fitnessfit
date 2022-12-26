
# from crypt import methods
# from crypt import methods
from email.message import Message
from re import S
from tokenize import Name
from unittest import result
from colorama import Cursor
from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql


# def execute():
#  print("In execute function")
#  conn=pymysql.connect(host='localhost',
#                        port=3306,
#                        user='root',
#                        db='fitness',
#                        password='')
#  print("connection established")
#  cursor=conn.cursor()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/fitness'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Register(db.Model):
    def __init__(self, Name, Age, Gender, Locality):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Locality = Locality

    sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    Age = db.Column(db.Integer)
    Gender = db.Column(db.String(50), nullable=False)
    Locality = db.Column(db.String(50), nullable=False)


class Contact(db.Model):
    def __init__(self,Name,Email,Message):
        self.Name=Name
        self.Email=Email
        self.Message=Message

    Sno=db.Column(db.Integer, primary_key=True)
    Name=db.Column(db.String(50),nullable=False)
    Email=db.Column(db.String(50),nullable=False)     
    Message=db.Column(db.String(50),nullable=False)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/about')
def about():

    print("hello")
    return render_template("about.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if(request.method == 'POST'):
        Name = request.form['a']
        Age = request.form['b']
        Gender = request.form['c']
        Locality = request.form['d']
        entry = Register(Name, Age, Gender, Locality)
        db.session.add(entry)
        db.session.commit()

        a = registration_display()
        return a
    return render_template("register.html")


@app.route('/detailshow', methods=['GET', 'POST'])
def registration_display():

    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           db='fitness',
                           password='')

    # print("connection established")            
    cursor = conn.cursor()            
    sql = "select * from register"         
    cursor.execute(sql)                                      
    result = cursor.fetchall()                                    
    print(result)                     
    conn.commit()                               

    return render_template("detailshow.html", result=result)   


@app.route('/contact',methods=['GET','POST'])
def contact():
    if (request.method == 'POST'):
        Name=request.form['name']
        Email=request.form['email']
        Message=request.form['message']
        entry=Contact(Name,Email,Message)
        db.session.add(entry)
        db.session.commit()
        b=contact_display()
        return b
    return render_template("contact.html") 

@app.route('/contactshow',methods=['GET','POST'])
def contact_display():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           db='fitness',
                           password='')

    cursor = conn.cursor()            
    sql = "select * from contact"         
    cursor.execute(sql)                                      
    ans = cursor.fetchall()                                    
    print(ans)                     
    conn.commit()                                        

    return render_template("contactshow.html") 



@app.route('/fitnesscalculator', methods=['GET','POST'])
def calculate():
    bmi=' '
    if (request.method == 'POST' ):  
        # print("In if block")      
        Weight =float( request.form['a'])       
        Height = float(request.form['b'])
        bmi=round(Weight/((Height/100)**2),2)
        return render_template("bmi.html",bmi=bmi,Weight=Weight,Height=Height)
    else:
         return render_template("fitnesscalculator.html")        


# @app.route('/bmi', methods=['GET', 'POST'])      
# def bmi():
       

#     return render_template("bmi.html",Weight=Weight,Height=Height)     
# @app.route('/contact')
# def contact():

#     print("hello")
#     return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
