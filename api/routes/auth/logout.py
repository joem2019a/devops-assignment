from flask import request, jsonify
from flask_praetorian import auth_required

from .. import routes
from api.middleware import auth
from api.utils import jti_blacklist


@routes.route('/auth/logout', methods=['POST'])
@auth_required
def logout():
  body = flask.request.get_json(force=True)
  data = guard.extract_jwt_token(body["token"])
  blacklist.add(data["jti"])
  return flask.jsonify(message="token blacklisted ({})".format(body["token"]))
