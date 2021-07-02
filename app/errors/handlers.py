from flask import jsonify
from werkzeug.exceptions import (
    BadRequest as WEBadRequest, NotFound as WENotFound
)

def handle_json_error(error):
    return jsonify(error.description), error.code

def BadRequest(app):
    app.errorhandler(WEBadRequest)(handle_json_error)

def NotFound(app):
    app.errorhandler(WENotFound)(handle_json_error)
