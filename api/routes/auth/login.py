from flask import request
from flask_praetorian import PraetorianError

from .. import routes
from api.middleware import auth


@routes.route('/auth/login', methods=['POST'])
def login():
  body = request.get_json()

  user = auth.authenticate(body['username'], body['password'])

  if not user.is_active:
    raise PraetorianError('Unauthorised.')

  return {
    'access_token': auth.encode_jwt_token(
      user,
      username=user.username,
      email=user.email,
    )
  }
