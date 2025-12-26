from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, open_user_notes, open_user_notes, save_notes

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Check if request method is POST
    if request.method == "POST":

        # Get data from form
        name = request.form.get("username")
        password = request.form.get("password")
        re_entered_password = request.form.get("confirmation")

        # Ensure username is submitted
        if not name:
            flash("must provide username")
            return render_template("register.html")
        # Ensure password is submitted
        elif not password:
            flash("must provide password")
            return render_template("register.html")
        # Ensure pasword is re-entered
        elif not re_entered_password:
            flash("must re-enter password")
            return render_template("register.html")

        # Ensure re-entered password matches with password
        elif password != re_entered_password:
            flash("re-entered password does not match")
            return render_template("register.html")

        # Hash the user’s password
        password_hash = generate_password_hash(password)

        # Insert user into database if username does not exist already
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)", name, password_hash
            )
            flash("Succesfully Registered")
            return render_template("register.html")

        except ValueError:
            flash("user name already taken, please use a different username")
            return render_template("register.html")

    else:
        # If request method is GET
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
            flash("Username required")
            return render_template("login.html")
        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("password required")
            return render_template("login.html")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("invalid username and/or password")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/")
@login_required
def index():
    """Show Notes"""

    # User_id of logged-in user
    user_id = session["user_id"]

    # Fetch user's Notes
    notes_dictionary = open_user_notes(user_id)

    return render_template("index.html", notes_dictionary=notes_dictionary)


@app.route("/addnote", methods=["GET", "POST"])
@login_required
def addnote():
    """Add Note to collection"""

    # User_id of logged-in user
    user_id = session["user_id"]

    # Check if request method is POST
    if request.method == "POST":

        # Get title from user
        title = request.form.get("title").upper()
        # Ensure title is given by user
        if not title:
            flash("Please enter Title")
            return render_template("addnote.html")

        # Get detail from user
        detail = request.form.get("detail")

        # Add note to collection
        notes_dictionary = open_user_notes(user_id)
        notes_dictionary[title] = detail

        # Save file
        save_notes(user_id, notes_dictionary)

        return redirect("/")

    else:
        # Renders buy page(user request via GET)
        return render_template("addnote.html")


@app.route("/removenote", methods=["GET", "POST"])
@login_required
def removenote():
    """Remove Note from collection"""

    # User_id of logged-in user
    user_id = session["user_id"]

    # Check if request method is POST
    if request.method == "POST":

        # Get title from user
        title = request.form.get("title")
        # Ensure title is given by user
        if not title:
            flash("Please enter Title")
            return render_template("addnote.html")

        # Delete note from collection
        notes_dictionary = open_user_notes(user_id)
        del notes_dictionary[title]

        # Save file
        save_notes(user_id, notes_dictionary)

        return redirect("/")

    else:
        # If requested via GET
        notes_dictionary = open_user_notes(user_id)

        return render_template("removenote.html", notes_dictionary=notes_dictionary)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
