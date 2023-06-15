from flask import Blueprint, render_template, request, redirect, jsonify, make_response
views = Blueprint("views", __name__)
from flask_wtf import FlaskForm, csrf
from netmiko import ConnectHandler

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/globalcommands")
def global_commands():
    return render_template("global_commands.html")

@views.route("/showcommands")
def show_commands():
    return render_template("show_commands.html")

@views.route("/privcommands")
def priv_commands():
    return render_template("priv_commands.html")

@views.route("/upload")
def upload():
    return render_template("upload.html")

@views.route("/loginpage")
def login():
    return render_template("login.html")


