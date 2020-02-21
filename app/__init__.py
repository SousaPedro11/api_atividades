from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
Bootstrap(app)

from app.controller.database_manipulation import database_manipulation as database_manipulaton_blueprint
from app.controller.home import home as home_blueprint

app.register_blueprint(database_manipulaton_blueprint)
app.register_blueprint(home_blueprint)

from app.model import tables

db.create_all()
