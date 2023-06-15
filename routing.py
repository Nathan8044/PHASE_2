from flask import Blueprint, render_template, request, redirect, jsonify, make_response
from flask_wtf import FlaskForm, csrf
from netmiko import ConnectHandler


routing_blueprint = Blueprint(__name__, 'routing')

@routing_blueprint.route("/routing", methods=["POST", "GET"])

def routing():

    return render_template("routing.html")
@routing_blueprint.route("/routing/config", methods=["POST"])
def routing_config 
    if request.method == 'POST':


