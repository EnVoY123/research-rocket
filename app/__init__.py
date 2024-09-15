from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('app.config.app_config')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes, models
with app.app_context():
    db.create_all()
