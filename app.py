from flask import Flask, render_template
from views import views 
from flask_wtf import FlaskForm, csrf
from interfacechanges import interfacechanges_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'NESMOS'
csrf.CSRFProtect(app)

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(interfacechanges_blueprint, url_prefix="/interfacechanges")


if __name__ == '__main__':
    app.run(debug=True, port=8000)