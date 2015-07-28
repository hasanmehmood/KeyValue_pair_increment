from flask import Flask

# Loading all configurations to flask app
app = Flask(__name__)
app.config.from_object('app.settings')

from app.models import KeyValue
from app.resources import keyvalue
from app import routes, views
