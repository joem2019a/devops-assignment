from flask import request, jsonify
from flask_praetorian import auth_required

from .. import routes
from api.middleware import auth
from api.utils import jti_blacklist


@routes.route('/auth/logout', methods=['POST'])
@auth_required
def logout():
  body = request.get_json(force=True)
  data = auth.extract_jwt_token(body["token"])
  jti_blacklist.add(data["jti"])
  return jsonify(message="token blacklisted ({})".format(body["token"]))
