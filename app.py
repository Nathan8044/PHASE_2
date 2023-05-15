from flask import Flask
from views import views
from interface_changes import interface_changes_blueprint


app = Flask(__name__)

app.register_blueprint(views, url_prefix="/home")

app.register_blueprint(interface_changes_blueprint, url_prefix="/interface_changes") #this is the interface_changes_blueprint


if __name__ == '__main__':
    app.run(debug=True, port=8000)