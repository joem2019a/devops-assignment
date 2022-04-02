from flask import request
from flask_praetorian import PraetorianError

from .. import routes
from api.middleware import auth


@routes.route('/api/auth/login', methods=['POST'])
def login():
  body = request.get_json()

  user = auth.authenticate(body['username'], body['password'])

  if not user.is_enabled:
    raise PraetorianError('Unauthorised.')

  return {
    'access_token': auth.encode_jwt_token(
      user,
      username=user.username,
      email=user.email,
      name=user.name,
      isAdmin=user.is_admin,
    )
  }
