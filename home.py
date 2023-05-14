from flask import Blueprint, render_template, request

home = Blueprint(__name__, "home")



@home.route("/")
def home():
    return render_template("index.html")

