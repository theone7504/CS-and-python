from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from flask_wtf import CSRFProtect
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from cs50 import SQL

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Set a secret key for session management
db = SQL("sqlite:///users.db")  # Connect to your SQLite database
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

csrf = CSRFProtect(app)  # Initialize CSRF protection

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/delete_task", methods=["POST"])
@login_required
def delete_task():
    task_id = request.form.get("task_id")
    if not task_id:
        return jsonify({"error": "must provide task ID"}), 403

    user_id = session["user_id"]
    db.execute("DELETE FROM Tasks WHERE task_id = ? AND user_id = ?", task_id, user_id)

    tasks = db.execute("SELECT * FROM Tasks WHERE user_id = ?", user_id)
    return jsonify(tasks)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return "must provide username", 403
        elif not password:
            return "must provide password", 403
        elif password != confirmation:
            return "passwords do not match", 403

        password_hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO Users (username, password_hash) VALUES(?, ?)", username, password_hash)
        except:
            return "username already exists", 403

        return redirect("/login")
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return "must provide username", 403
        elif not password:
            return "must provide password", 403

        rows = db.execute("SELECT * FROM Users WHERE username = ?", username)

        if len(rows) != 1 or not check_password_hash(rows[0]["password_hash"], password):
            return "invalid username and/or password", 403

        session["user_id"] = rows[0]["user_id"]
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/", methods=["GET", "POST"])
@login_required
def tasks():
    user_id = session["user_id"]

    if request.method == "POST":
        task_name = request.form.get("task_name")
        task_description = request.form.get("task_description")
        priority = request.form.get("priority")
        due_date = request.form.get("due_date")

        if not task_name:
            return jsonify({"error": "must provide task name"}), 403

        db.execute("INSERT INTO Tasks (user_id, task_name, task_description, priority, due_date) VALUES(?, ?, ?, ?, ?)",
                   user_id, task_name, task_description, priority, due_date)

        tasks = db.execute("SELECT * FROM Tasks WHERE user_id = ?", user_id)
        return jsonify(tasks)

    else:
        tasks = db.execute("SELECT * FROM Tasks WHERE user_id = ?", user_id)
        return render_template("tasks.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Use port
