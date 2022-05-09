import os
import psycopg2
import sqlalchemy
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from flask_mail import Mail, Message
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///lab.db")
# Use this for pushing to Heroku
database_url = os.environ.get('DATABASE_LOC')

# Use this for local
#database_url = ("postgresql://postgres:Afr1ca7win1100D4!@localhost:5432/lab")

# Use this for both local and Heroku
db = SQL(database_url)
# db.execute("PRAGMA foreign_keys = ON")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Setup email
app.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL_DEFAULT_SENDER"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp-relay.sendinblue.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
mail = Mail(app)

# <!--index, request, completed, active routes below -->

@app.route("/")
@app.route("/index")
# @login_required
def index():
    """start page"""
    return render_template('index.html')

@app.route("/request_exp", methods=["GET", "POST"])
@login_required
def request_exp():
    """Request a development - customer facing"""
    if request.method == "POST":

        # Get company name from request_ext
        cust_id = request.form.get("company")

        # Get company ID to set session
        rows = db.execute("SELECT * FROM customers WHERE id = ?;", cust_id)
        session["cust_id"] = rows[0]["id"]

        # Move on to address request page
        return redirect("request_exp2")

    else:
        # If request.method == "GET" send a list of all customers in the table to form
        company_list = db.execute("SELECT id, company FROM customers ORDER BY company;")
        return render_template("request_exp.html", company_list=company_list)

@app.route("/request_std", methods=["GET", "POST"])
@login_required
def request_std():
    """Request a standard - customer facing"""
    if request.method == "POST":

        # Get company name from request_ext
        cust_id = request.form.get("company")

        # Get company ID to set session
        rows = db.execute("SELECT * FROM customers WHERE id = ?;", cust_id)
        session["cust_id"] = rows[0]["id"]

        # Move on to address request page
        return redirect("request_std2")

    else:
        # If request.method == "GET" send list of all customers in table to the form
        company_list = db.execute("SELECT id, company FROM customers ORDER BY company;")
        return render_template("request_std.html", company_list=company_list)

@app.route("/request_exp2", methods=["GET", "POST"])
@login_required
def request_exp2():
    """Enter a development request part 2"""
    if request.method =="POST":

        # Get company address from request_ext2
        add_id = request.form.get("address")

        # Get address ID to set session
        rows  = db.execute("SELECT * FROM addresses WHERE id = ?;", add_id)
        session["add_id"] = rows[0]["id"]

        # Move on to contact request page
        return redirect("request_exp3")

    else:
        # If request.method == "GET" send a list of all addresses associated with that customer
        address_list = db.execute("SELECT * FROM addresses WHERE cust_id = ?;", session["cust_id"])
        return render_template("request_exp2.html", address_list=address_list)

@app.route("/request_std2", methods=["GET", "POST"])
@login_required
def request_std2():
    """Enter a development request part 2"""
    if request.method =="POST":

        # Get company address from request_ext2
        add_id = request.form.get("address")

        # Get address ID to set session
        rows  = db.execute("SELECT * FROM addresses WHERE id = ?;", add_id)
        session["add_id"] = rows[0]["id"]

        # Move on to contact request page
        return redirect("request_std3")

    else:
        # If request.method == "GET" send a list of all addresses associated with that customer
        address_list = db.execute("SELECT * FROM addresses WHERE cust_id = ?;", session["cust_id"])
        return render_template("request_std2.html", address_list=address_list)

@app.route("/request_exp3", methods=["GET", "POST"])
@login_required
def request_exp3():
    """Enter a development request part 3"""
    if request.method =="POST":

        # Get contact name from request_ext3
        contact_id = request.form.get("contact")

        # Get contact ID to set session
        rows  = db.execute("SELECT * FROM contacts WHERE id = ?;", contact_id)
        session["contact_id"] = rows[0]["id"]

        # Move on to final development request page
        return redirect("request_exp4")

    else:
        # If request.method == "GET" return a list of all contacts associated with cust_id
        contact_list = db.execute("SELECT * FROM contacts WHERE cust_id = ?;", session["cust_id"])
        return render_template("request_exp3.html", contact_list=contact_list)

@app.route("/request_std3", methods=["GET", "POST"])
@login_required
def request_std3():
    """Enter a development request part 3"""
    if request.method =="POST":

        # Get contact name from request_ext
        contact_id = request.form.get("contact")

        # Get contact ID to set session
        rows  = db.execute("SELECT * FROM contacts WHERE id = ?;", contact_id)
        session["contact_id"] = rows[0]["id"]

        # Move on to final development request page
        return redirect("request_std4")

    else:
        # If request.method == "GET" return a list of all contacts associated with cust_id
        contact_list = db.execute("SELECT * FROM contacts WHERE cust_id = ?;", session["cust_id"])
        return render_template("request_std3.html", contact_list=contact_list)

@app.route("/request_exp4", methods=["GET", "POST"])
@login_required
def request_exp4():
    """Enter a development request part 4"""
    if request.method =="POST":
        cust_id = session["cust_id"]
        add_id = session["add_id"]
        contact_id = session["contact_id"]
        request_user_id = session["user_id"]
        priority = request.form.get("priority")
        date_required = request.form.get("date_required")
        exp_descrip = request.form.get("exp_descrip")
        process = request.form.get("process")
        ship_request_method = request.form.get("ship_request_method")
        part_descrip = request.form.get("part_descrip")
        color = request.form.get("color")
        material_type = request.form.get("material_type")
        clr_filled = request.form.get("clr_filled")
        supplied_mat = request.form.get("supplied_mat")
        match_type = request.form.get("match_type")
        pantone = request.form.get("pantone")
        exact = request.form.get("exact")
        sample_size = request.form.get("sample_size")
        finish = request.form.get("finish")
        fda = request.form.get("fda")
        other_reg = request.form.get("other_reg")
        cure_type = request.form.get("cure_type")
        cure_time = request.form.get("cure_time")
        cure_temp = request.form.get("cure_temp")
        pc_time = request.form.get("pc_time")
        pc_temp = request.form.get("pc_temp")
        internal = request.form.get("internal")
        customerlist = db.execute("SELECT company FROM customers WHERE id = ?;", cust_id)
        customer = customerlist[0]["company"]

        # insert request into devrequest table
        db.execute("INSERT INTO devrequest (cust_id, add_id, contact_id, request_user_id, priority, date_required, exp_descrip, process, ship_request_method, part_descrip, color, material_type, clr_filled, supplied_mat, match_type, pantone, exact, sample_size, finish, fda, other_reg, cure_type, cure_time, cure_temp, pc_time, pc_temp, internal) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
                   , cust_id, add_id, contact_id, request_user_id, priority, date_required, exp_descrip, process, ship_request_method, part_descrip, color, material_type, clr_filled, supplied_mat, match_type, pantone, exact, sample_size, finish, fda, other_reg, cure_type, cure_time, cure_temp, pc_time, pc_temp, internal)


        # Email the new development request to everyone
        message = Message("A new Development Request has been submitted!", recipients = ['kclab@kri-color.com'])
        message.html = "<b>NEW DEVELOPMENT REQUEST</b> <p><b>Customer: </b>{}</p> <p><b>Priority: </b>{}</p> <p><b>Date Required: </b>{}</p> <p><b>Description: </b>{}</p> <p><b>Ship Method: </b>{}</p> <p><b>Requested By: </b>{}</p>".format(customer, priority, date_required, exp_descrip, ship_request_method, session["username"])
        mail.send(message)

        # Show the user that the project was successfully logged
        flash('Project Submitted Successfully')
        return render_template('success.html')

    else:
        # If request.method == "GET":
        # Return all gathered company info from previous three sections to return to development request page for output
        company_info = db.execute("SELECT customers.id, customers.company as company, addresses.id, addresses.add1, addresses.add2, addresses.city, addresses.state, addresses.zip, addresses.country, contacts.id, contacts.firstname, contacts.lastname, contacts.phone, contacts.email FROM customers JOIN addresses ON customers.id = addresses.cust_id JOIN contacts ON customers.id = contacts.cust_id WHERE customers.id = ? and addresses.id = ? and contacts.id = ?;", session["cust_id"], session["add_id"], session["contact_id"])
        return render_template("request_exp4.html", company_info = company_info)

@app.route("/request_std4", methods=["GET", "POST"])
@login_required
def request_std4():
    """Enter a standard request part 4"""
    if request.method =="POST":
        cust_id = session["cust_id"]
        add_id = session["add_id"]
        contact_id = session["contact_id"]
        request_user_id = session["user_id"]
        product = request.form.get("product")
        priority = request.form.get("priority")
        date_required = request.form.get("date_required")
        std_descrip = request.form.get("std_descrip")
        ship_request_method = request.form.get("ship_request_method")
        sample_size = request.form.get("sample_size")
        customerlist = db.execute("SELECT company FROM customers WHERE id = ?;", cust_id)
        customer = customerlist[0]["company"]

        # insert request into stdrequest table
        db.execute("INSERT INTO stdrequest (cust_id, add_id, contact_id, request_user_id, priority, date_required, std_descrip, product, ship_request_method, sample_size) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
                   , cust_id, add_id, contact_id, request_user_id, priority, date_required, std_descrip, product, ship_request_method, sample_size)

        # Email everyone that a new standard request has been submitted
        message = Message("A new Sample Request has been submitted!", recipients = ['kclab@kri-color.com'])
        message.html = "<b>NEW SAMPLE REQUEST</b> <p><b>Customer: </b>{}</p> <p><b>Product: </b>{}</p> <p><b>Priority: </b>{}</p> <p><b>Date Required: </b>{}</p> <p><b>Description: </b>{}</p> <p><b>Ship Method: </b>{}</p> <p><b>Sample Size: </b>{}</p> <p><b>Requested By: </b>{}</p>".format(customer, product, priority, date_required, std_descrip, ship_request_method, sample_size, session["username"])
        mail.send(message)

        # Show the user that the project was successfully logged
        flash('Sample Request Submitted Successfully')
        return render_template('success.html')

    else:
        # If request.method == "GET":
        # Return all gathered company info from previous three sections to return to development request page for output
        company_info = db.execute("SELECT customers.id, customers.company as company, addresses.id, addresses.add1, addresses.add2, addresses.city, addresses.state, addresses.zip, addresses.country, contacts.id, contacts.firstname, contacts.lastname, contacts.phone, contacts.email FROM customers JOIN addresses ON customers.id = addresses.cust_id JOIN contacts ON customers.id = contacts.cust_id WHERE customers.id = ? and addresses.id = ? and contacts.id = ?;", session["cust_id"], session["add_id"], session["contact_id"])
        return render_template("request_std4.html", company_info = company_info)


@app.route("/experiments")
@login_required
def experiments():
    """List of all open experiment development requests - external facing"""
    data = db.execute("SELECT * FROM devrequest JOIN customers ON devrequest.cust_id = customers.id JOIN contacts ON devrequest.contact_id = contacts.id JOIN users ON devrequest.request_user_id = users.id WHERE devrequest.date_completed is null and devrequest.internal <> 'Yes'  ORDER BY devrequest.date_required, devrequest.priority;")
    return render_template('experiments.html', tableA = data)

@app.route("/internals")
@login_required
def internals():
    """List of all open experiment development requests - internal facing"""
    data = db.execute("SELECT * FROM devrequest JOIN customers ON devrequest.cust_id = customers.id JOIN contacts ON devrequest.contact_id = contacts.id JOIN users ON devrequest.request_user_id = users.id WHERE devrequest.date_completed is null and devrequest.internal <> 'No'  ORDER BY devrequest.date_required, devrequest.priority;")
    return render_template('internals.html', tableA = data)

@app.route("/stds")
@login_required
def stds():
    """Request a standard sample or colorbook"""
    data = db.execute("SELECT * FROM stdrequest JOIN customers ON stdrequest.cust_id = customers.id JOIN contacts ON stdrequest.contact_id = contacts.id JOIN users ON stdrequest.request_user_id = users.id WHERE stdrequest.date_completed is null ORDER BY stdrequest.date_required, stdrequest.priority;")
    return render_template('stds.html', tableA = data)

@app.route("/history")
@login_required
def history():
    """List of all closed out development requests"""
    data = db.execute("SELECT * FROM devrequest JOIN customers ON devrequest.cust_id = customers.id JOIN contacts ON devrequest.contact_id = contacts.id JOIN users ON devrequest.request_user_id = users.id WHERE devrequest.date_completed is not null and devrequest.internal <> 'Yes'  ORDER BY devrequest.date_required, devrequest.priority;")
    return render_template('history.html', tableA = data)

@app.route("/hist_stds")
@login_required
def hist_stds():
    """List of all closed out standard requests"""
    data = db.execute("SELECT * FROM stdrequest JOIN customers ON stdrequest.cust_id = customers.id JOIN contacts ON stdrequest.contact_id = contacts.id JOIN users ON stdrequest.request_user_id = users.id WHERE stdrequest.date_completed is not null ORDER BY stdrequest.date_required, stdrequest.priority;")
    return render_template('hist_stds.html', tableA = data)

@app.route("/add_cust", methods=['POST'])
def add_cust():
    # Get company name from modal
    company = request.form.get("company")

    #Add into database
    db.execute("INSERT INTO customers (company) VALUES(?);", company)
    return redirect("request_exp")

@app.route("/add_add", methods=['POST'])
def add_add():
    # Get company address from modal
    add1 = request.form.get("add1")
    add2 = request.form.get("add2")
    city = request.form.get("city")
    state = request.form.get("state")
    zip = request.form.get("zip")
    country = request.form.get("country")

    #Add into database
    db.execute("INSERT INTO addresses (add1, add2, city, state, zip, country, cust_id) VALUES(?, ?, ?, ?, ?, ?, ?);", add1, add2, city, state, zip, country, session["cust_id"])
    return redirect("request_exp2")

@app.route("/add_contact", methods=['POST'])
def add_contact():
    # Get company contact info from modal
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    phone = request.form.get("phone")
    email = request.form.get("email")

    #Add into database
    db.execute("INSERT INTO contacts (firstname, lastname, phone, email, cust_id) VALUES(?, ?, ?, ?, ?);", firstname, lastname, phone, email, session["cust_id"])
    return redirect("request_exp3")

@app.route("/signoff", methods=["GET", "POST"])
@login_required
def signoff():
    # If request method is POST, insert the signoff info from signoff page to devrequest table.
    if request.method == "POST":
        date_completed = request.form.get("date_completed")
        matched = request.form.get("matched")
        pphr_percent = request.form.get("pphr_percent")
        exp_number = request.form.get("exp_number")
        com_number = request.form.get("com_number")
        total_hours = request.form.get("total_hours")
        shipping_company = request.form.get("shipping_company")
        ship_tracking = request.form.get("ship_tracking")
        notes = request.form.get("notes")

        # Update the devrequest table with new information
        db.execute("UPDATE devrequest SET date_completed = ?, matched = ?, pphr_percent = ?, exp_number = ?, com_number = ?, total_hours = ?, shipping_company = ?, ship_tracking = ?, notes = ?, completed_user_id = ? WHERE dr_id = ?;", date_completed, matched, pphr_percent, exp_number, com_number, total_hours, shipping_company, ship_tracking, notes, session["user_id"], session["record_ids"])
        
        # Email everyone that a new development request has been submitted
        message = Message("A Development Request has been completed!", recipients = ['kclab@kri-color.com'])
        message.html = "A Development request has been completed. <p><b>Shipped by: </b>{}</p> <p><b>Tracking number: </b>{}</p> <p><b>Signed Off By: </b>{}</p>".format(shipping_company, ship_tracking, session["username"])
        mail.send(message)
        
        # Return user back to the open experiments table
        return redirect("experiments")
    else:
        # If for some reason, no record is returned, return an apology.
        session["record_ids"] = request.args.get("record_id")
        if not session["record_ids"]:
            return apology("no record")

        # If request method is GET, Get record ID from the row in open experiments page after clicking signoff
        else:
            results = db.execute("SELECT * FROM devrequest JOIN customers ON devrequest.cust_id = customers.id JOIN contacts ON devrequest.contact_id = contacts.id WHERE dr_id = ?;", session["record_ids"])
            return render_template("signoff.html", results=results)

@app.route("/std_signoff", methods=["GET", "POST"])
@login_required
def std_signoff():
    # If request method is POST, insert the signoff info from signoff page to devrequest table.
    if request.method == "POST":
        date_completed = request.form.get("date_completed")
        shipping_company = request.form.get("shipping_company")
        ship_tracking = request.form.get("ship_tracking")

        db.execute("UPDATE stdrequest SET date_completed = ?, shipping_company = ?, ship_tracking = ?, completed_user_id = ? WHERE std_id = ?;", date_completed, shipping_company, ship_tracking, session["user_id"], session["record_ids"])
        
        # Email everyone that a new standard request has been signed off
        message = Message("A Standard Request has been completed!", recipients = ['kclab@kri-color.com'])
        message.html = "A standard sample request has been completed. <p><b>Shipped by: </b>{}</p> <p><b>Tracking number: </b>{}</p> <p><b>Signed Off By: </b>{}</p>".format(shipping_company, ship_tracking, session["username"])
        mail.send(message)

        # Return user back to open standard requests
        return redirect("stds")
    else:
        # If for some reason, no record is returned, return an apology.
        session["record_ids"] = request.args.get("record_id")
        if not session["record_ids"]:
            return apology("no record")
        # If request method is GET, Get record ID from the row in open experiments page after clicking signoff
        else:
            results = db.execute("SELECT * FROM stdrequest JOIN customers ON stdrequest.cust_id = customers.id JOIN contacts ON stdrequest.contact_id = contacts.id WHERE std_id = ?;", session["record_ids"])
            return render_template("std_signoff.html", results=results)

# <!--all user register, login, logout routes below-->

@app.route("/users")
@login_required
def users():
    users = db.execute("SELECT * FROM users ORDER BY id")
    return render_template("users.html", users=users)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Get username and password from form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        useremail = request.form.get("useremail")

        # get info from users database to see if there is a user
        usernameCheck = db.execute("SELECT * FROM users WHERE username = ?;", username)

        # Validate that username, password, and confirmation are ok
        if not username or not password or not confirmation or password != confirmation:
            return apology("invalid username or password or password doesn't match confirmation")

        # elif username is already taken
        elif len(usernameCheck) == 1:
            return apology("Username already taken")

        else:
            # insert username info into database
            db.execute("INSERT INTO users (username, hash, firstname, lastname, useremail) VALUES(?, ?, ?, ?, ?);", username, generate_password_hash(password), firstname, lastname, useremail)

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = ?;", username)

            # start session
            session["user_id"] = rows[0]["id"]
            session["username"] = rows[0]["username"]
            session["useremail"] = rows[0]["useremail"]
            name = rows[0]["firstname"]

            # Email the new registrant
            message = Message("You are registered with KC Lab Database!", recipients = [session["useremail"]])
            message.body = "Hey {}, you have successfully registered in the KCLAB dB. Do not respond to this email.".format(name)
            mail.send(message)

           # return to index
            return redirect("/")
    else:
        # If request.method == "GET":
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]
        session["useremail"] = rows[0]["useremail"]

        # If user is an admin, set admin session
        if rows[0]["adm"] == True:
            session["admin"] = rows[0]["adm"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":

        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        useremail = request.form.get("useremail")

        # Validate that username, password, and confirmation are ok
        if not password or not confirmation or password != confirmation:
            return apology("invalid password or password doesn't match confirmation")

        # insert username info into database
        db.execute("UPDATE users SET hash = ?, firstname = ?, lastname = ?, useremail = ? WHERE id = ?;", generate_password_hash(password), firstname, lastname, useremail, session["user_id"])
        
        # Show the user that the project was successfully logged
        flash('Profile Successfully Updated')
        return render_template('success.html')

    # if request.method == "GET" select user info from user table and return to form.
    user_info =  db.execute("SELECT firstname, lastname, useremail FROM users WHERE id = ?;", session["user_id"])
    return render_template("profile.html", user_info = user_info)