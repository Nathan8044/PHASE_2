from flask import Blueprint, render_template, request, redirect, jsonify, make_response
views = Blueprint("views", __name__)
from flask_wtf import FlaskForm, csrf
from netmiko import ConnectHandler

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/privcommands")
def priv_commands():
    return render_template("priv_commands.html")

@views.route("/loginpage")
def login():
    return render_template("login.html")


