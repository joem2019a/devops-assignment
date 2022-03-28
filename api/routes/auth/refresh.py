from flask import jsonify

from .. import routes
from api.middleware import auth


@routes.route('/auth/refresh', methods=['GET'])
def refresh():
  old_token = auth.read_token_from_header()
  new_token = auth.refresh_jwt_token(old_token)

  return jsonify(access_token=new_token)
