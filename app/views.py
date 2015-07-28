import os
from flask import send_from_directory

from flask_restful import reqparse, abort, Api, Resource, fields, marshal
from flask import jsonify

from app import app
from app.common.util import abort_if_record_doesnt_exist
from app.models.KeyValue import KeyValue

# Index Page!
@app.route('/')
@app.route('/index')
def index():
    return "Welcome to Increment Key Value Pair API, Hassan Mehmood!"