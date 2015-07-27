import datetime

from flask.ext.mongoengine import MongoEngine
from mongoengine import *
from app import app


db = MongoEngine(app)

# Model for storing all Key Value Pairs
class KeyValue(db.Document):
	
	key = StringField(max_length=50, required=True)
	value = IntField(required=True)
	created_at = DateTimeField(default=datetime.datetime.now)

