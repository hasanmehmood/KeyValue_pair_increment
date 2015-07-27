
from flask import jsonify, url_for, request, make_response
from flask.ext.restful import reqparse, abort
from app.models.KeyValue import KeyValue


#### Helper Functions ####

def abort_if_record_doesnt_exist(key, entity):
    if entity is None:
        abort(404, message="Key '{}' doesn't exist".format(key)) 


def error_response(code, message):
    return jsonify({'status': False, 'error': {
		            'code': code,
		            'message': message
		    }})
