# All Routes will be define in this file

from flask.ext import restful
from app import app
from app.resources.keyvalue import KeyValueCreateAPI, KeyValueAPI 

api = restful.Api(app)

# Configuring Routes for defined API classes
api.add_resource(KeyValueCreateAPI, '/api/v1/keyvalue')
api.add_resource(KeyValueAPI, '/api/v1/keyvalue/<key>')
