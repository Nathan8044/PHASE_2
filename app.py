from flask import Flask, render_template
from views import views 
from flask_wtf import FlaskForm, csrf
from interfacechanges import interfacechanges_blueprint
from interfacesecurity import interfacesecurity_blueprint
from routing import routing_blueprint
from global_commands import global_commands_blueprint
from showcommands import showcommands_blueprint
from upload import upload_blueprint




app = Flask(__name__)
app.config['SECRET_KEY'] = 'NESMOS'
csrf.CSRFProtect(app)

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(interfacechanges_blueprint, url_prefix="/interfacechanges")
app.register_blueprint(interfacesecurity_blueprint, url_prefix="/interfacesecurity")
app.register_blueprint(routing_blueprint, url_prefix="/routing")
app.register_blueprint(global_commands_blueprint, url_prefix='/globalcommands')
app.register_blueprint(showcommands_blueprint, url_prefix='/showcommands')
app.register_blueprint(upload_blueprint, url_prefix='/upload')


if __name__ == '__main__':
    app.run(debug=True, port=8000)