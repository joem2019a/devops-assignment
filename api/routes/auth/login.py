from flask import request, jsonify

from .. import routes
from api.middleware import auth


@routes.route('/auth/login', methods=['POST'])
def login():
  body = request.get_json()

  user = guard.authenticate(body['username'], body['password'])

  return flask.jsonify(access_token=guard.encode_jwt_token(user))
