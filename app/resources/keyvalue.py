# Implementing all the routes here!

from flask_restful import reqparse, abort, Api, Resource, fields, marshal
from flask import jsonify

from app import app
from app.common.util import abort_if_record_doesnt_exist
from app.models.KeyValue import KeyValue

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('key', type=str)
parser.add_argument('value', type=int)


# KeyValueCreateAPI will creates new key value pair and stores them in the MongoDB
class KeyValueCreateAPI(Resource):

    def post(self):

        args = parser.parse_args()
        keyvalue = KeyValue(key=args['key'], value=args['value'])
        keyvalue.save()

        return { 'key': keyvalue.key,
                 'value': keyvalue.value }, 201               
        


# KeyValueAPI will provide you GET API for Gettin, updating or deleting a key value pair
class KeyValueAPI(Resource):

    def get(self, key):

        # incrementing using inc according to mongoengine
        KeyValue.objects(key=key).update(inc__value=1) 
        keyvalue = KeyValue.objects(key=key).first()
        abort_if_record_doesnt_exist(key, keyvalue)
        
        return { 'value': keyvalue.value }, 200

    def delete(self, key):

        keyvalue = KeyValue.objects(key=key).first()
        abort_if_record_doesnt_exist(key, keyvalue)
        keyvalue.delete()

        return { 'key': key, 
                 'status': 'deleted' }, 204

    def put(self, key):

        args = parser.parse_args()
        keyvalue = KeyValue.objects(key=key).first()
        abort_if_record_doesnt_exist(key, keyvalue)
        keyvalue.value = args['value']
        keyvalue.save()

        return { 'key': keyvalue.key,
                 'value': keyvalue.value }, 201



