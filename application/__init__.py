from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('config.Config')
csrf = CSRFProtect(app)
# db = MongoEngine(app)

from application.tech import controller