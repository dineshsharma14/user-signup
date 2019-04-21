from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template("index.html", title="Sign Up")


def space_checker(name):
    for char in name:
        if char == " ":
            return True
    return False


def char_count_checker(name):
    counter = 0
    for char in name:
        counter += 1
    if counter < 3 or counter > 20:
        return True
    else:
        return False


@app.route("/submission", methods=['POST'])
def submission():
    # Collecting details from user and processing 
    name = request.form['username']
    password1 = request.form['password1']
    password2 = request.form['password2']
    email = request.form['email']
    name_error, password1_error, password2_error, email_error = "", "", "", ""

    # Validation on Server side

    if name.strip() == "":
        name_error = "User name can't be left empty."
    elif space_checker(name):
        name_error = "User name can't have space character."
    elif char_count_checker(name):
        name_error = "User name can have only 3-20 chars."

    if password1.strip() == "":
        password1_error = "Password can't be left empty"
    elif space_checker(password1):
        password1_error = "Password can't have space character."
    elif char_count_checker(password1):
        password1_error = "Password can have only 3-20 chars."

    if password2.strip() == "":
        password2_error = "Password can't be left empty"
    elif password1 != password2:
        password1_error = ""
        password2_error = "Passwords not matching"
    elif space_checker(password2):
        password2_error = "Password can't have space character."
    
    if email.strip() == "":
        pass
    else:
        if char_count_checker(email):
            email_error = "Email can have only 3 to 20 characters."
        elif space_checker(email):
            email_error = "Email can't have a space character."
        else: 
            count_at = 0
            for char in email:
                if char == "@":
                    count_at += 1
            if count_at > 1:
                email_error = "Email can't have more than one '@' character."
            count_period = 0
            for char in email:
                if char == ".":
                    count_period += 1
            if count_period > 1:
                email_error = "Email can't have more than one '.' character."

    return render_template("submission.html", title="Submission", name=name, email=email, name_error=name_error, password1_error=password1_error, password2_error=password2_error, email_error=email_error)
app.run()
