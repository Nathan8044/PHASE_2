from flask import Flask, render_template
from views import views 
from flask_wtf import FlaskForm, csrf


app = Flask(__name__)
app.config['SECRET_KEY'] = 'NESMOS'
csrf.CSRFProtect(app)

app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=8000)