from flask import Flask
from views import views
from main_functions import main_functions_blueprint

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/views")
app.register_blueprint(main_functions_blueprint, url_prefix="/main_functions")
#app.register_blueprint(interface_changes_blueprint, url_prefix="/interface_changes")



if __name__ == '__main__':
    app.run(debug=True, port=8000)