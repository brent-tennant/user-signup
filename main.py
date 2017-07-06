from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup-form.html')


@app.route("/", methods=['POST'])
def validate_fields():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    #Username too short or too long
    if len(username) < 3:
        username = ''
        username_error = 'Username must be more than 3 characters'
    elif len(username) > 20:
        username = ''
        username_error = 'Username must be less than 20 characters'
    else:
        username = username

    #Password too short or too long
    if 20 < len(password) < 3:
        password = ''
        password_error = 'Password must contain more than 3 character but no more than 20'

    #Passwords don't match
    if password != verify_password:
        password = ''
        verify_password = ''
        verify_password_error = 'Passwords do not match'

    #Email not valid
    if len(email) > 0:
        if not(email.endswith('@') or email.startswith('@') or email.endswith('.') or email.startswith('.')) and email.count('@') == 1 and email.count('.') == 1:
            email=email
        else:
            email = ''
            email_error = 'Email must contain @/. but not start or end with those characters'
    else:
        email = ''

    #Empty Fields
    if username == "":
        username_error = 'Username must be more than 3 characters but no more than 20'
    if password == "":
        password_error = 'Password must contain more than 3 character but no more than 20'
    if verify_password == "":
        verify_password_error = 'Passwords do not match'


    #Redirect to Confirmation Page if conditions are met
    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template('confirmation.html', username = username)

    #Returns to signup-form if any conditions are not met
    else:
        return render_template('signup-form.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error,
        username=username, password=password, verify_password=verify_password, email=email)

app.run()
