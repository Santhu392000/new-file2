from flask import Flask, render_template,request,redirect,url_for,session,flash
from sendgrid.helpers.mail import Mail

app=Flask(__name__)
app.secret_key='a'

    
@app.route("/")
def dash():
    return render_template('welcome.html',msg=" ")

    
    
@app.route('/login')
def login():
    return render_template("login.html",msg=" ")

@app.route('/welcome')
def welcome_page():
    return render_template("welcome.html",msg=" ")
@app.route('/home')
def home():
    return render_template("home.html",msg=" ")

@app.route('/register')
def register():
    return render_template("register.html",msg=" ")
    
@app.route('/skills')
def skills():
    return render_template("skills.html",msg=" ")
@app.route('/about')
def about():
    return render_template("about.html",msg=" ")
@app.route('/contact')
def contact():
    return render_template("contact.html",msg=" ")
if __name__=='__main__':
    app.run(debug=True)
