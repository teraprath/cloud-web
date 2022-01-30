from flask import Flask, render_template, redirect, url_for, request, send_file, session
from werkzeug.utils import secure_filename
from functions import convert_size, getData
import os
import database
import config

app = Flask(__name__)
app.config["SECRET_KEY"] = "uGa1CwRysEZPWzuNQ3hQDuNLaEqM3rvg"
app.config["UPLOAD_FOLDER"] = config.upload_folder

@app.route("/")
def index():
    if "loggedin" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if "loggedin" in session:
        return redirect(url_for("index"))
    else:
        if request.method == "POST":
            password = request.form["password"]
            if password != getData("password"):
                error = "Login failed."
                return render_template("pages/login.html", error=error)
            else:
                session["loggedin"] = True
                return redirect(url_for("index"))

        return render_template("pages/login.html")

@app.route("/logout")
def logout():
    session.pop("loggedin")
    return redirect(url_for("index"))

@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    files = database.fetchall()
    filter = False
    if request.method == "POST":
        req = request.form["search"]
        files = database.where(req)
        filter = req
    return render_template("pages/dashboard.html", files=files, filter=filter)

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if "loggedin" in session:
        if request.method == "POST":
            files = request.files.getlist("file")
            for file in files:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                size = os.path.getsize(app.config["UPLOAD_FOLDER"] + filename)
                database.insert(filename, convert_size(size))
            return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))

@app.route("/download/<path:filename>", methods=["POST", "GET"])
def download(filename):
    if "loggedin" in session:
        path = app.config["UPLOAD_FOLDER"] + filename
        return send_file(path, as_attachment=True)
    else:
        return redirect(url_for("login"))

@app.route("/delete/<path:filename>", methods=["POST", "GET"])
def delete(filename):
    if "loggedin" in session:
        path = app.config["UPLOAD_FOLDER"] + filename
        os.remove(path)
        database.delete(filename)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(port=5500, debug=True)