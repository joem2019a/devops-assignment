from flask import jsonify

from .. import routes
from api.middleware import auth


@routes.route('/auth/refresh', methods=['GET'])
def refresh():
  old_token = guard.read_token_from_header()
  new_token = guard.refresh_jwt_token(old_token)

  return flask.jsonify(access_token=new_token)
