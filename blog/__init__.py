from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '562616ff3cc8bfebd2d80917849cf27e16c2a0c9861aae22'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c22109083:ilovecats@csmysql.cs.cf.ac.uk:3306/c22109083_blog'
db = SQLAlchemy(app)



login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes

with app.app_context():
    db.create_all()