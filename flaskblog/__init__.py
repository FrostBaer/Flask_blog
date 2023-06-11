from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
#secret key against Cross-site scripting and alike
app.config['SECRET_KEY'] = '1676359920d707df5380cc553aea4b04'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db instance
db = SQLAlchemy(app)
# pw encryption
bcrypt = Bcrypt(app)
# login
login_manager = LoginManager(app)
# where to go if accessing a login_required page without authentication
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# nem felül, hogy ne legyen körkörös import
from flaskblog import routes