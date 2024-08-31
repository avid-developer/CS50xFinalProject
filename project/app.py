
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///personalbudgettracker.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "GET":
        budgets = db.execute("select name from budget where user_id = ?", session["user_id"])
        return render_template("index.html", budgets=budgets)
    else:
        budget_name = request.form.get("budget")
        budget_amount = db.execute("select amount from budget where user_id = ? and name = ?", session["user_id"], budget_name)
        budget_amount = budget_amount[0]['amount']
        expenses = db.execute("select category, sum(amount) as amount from expenses where user_id = ? and budget_name = ? group by category", session["user_id"], budget_name)
        total_expenses = db.execute("SELECT SUM(amount) as total FROM expenses WHERE user_id = ? AND budget_name = ?", session["user_id"], budget_name)
        total_expenses = total_expenses[0]['total']
        left = budget_amount - total_expenses

        return render_template("index2.html", amount=budget_amount, expenses=expenses, left=left)


@app.route("/budget", methods=["GET", "POST"])
@login_required
def budget():
    if request.method == "GET":
        return render_template("budget.html")

    else:
        budget = request.form.get("budget")
        amount = request.form.get("amount")
        amount = int(amount)
        db.execute("insert into budget (user_id, name, amount) values (?, ?, ?)", session["user_id"], budget, amount)

        return redirect("/")


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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


@app.route("/expense", methods=["GET", "POST"])
@login_required
def expense():
    if request.method == "GET":
        budgets = db.execute("select name from budget where user_id = ?", session["user_id"])
        return render_template("expense.html", budgets=budgets)

    else:
        budget = request.form.get("budget")
        category = request.form.get("category")
        amount = request.form.get("amount")
        amount = int(amount)

        db.execute("insert into expenses (user_id, budget_name, category, amount) values (?, ?, ?, ?)", session["user_id"], budget, category, amount)

        return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmtaion", 400)

        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("Password and confirmation password should match", 400)

        hashed_password = generate_password_hash(request.form.get("password"))

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) > 0:
            return apology("Username already taken", 400)

        db.execute(
            "insert into users (username, hash) values (?, ?)", request.form.get(
                "username"), hashed_password
        )

        user = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        session["user_id"] = user[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


