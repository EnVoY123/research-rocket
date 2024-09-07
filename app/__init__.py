from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('app.config.app_config')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes, models
with app.app_context():
    db.create_all()
