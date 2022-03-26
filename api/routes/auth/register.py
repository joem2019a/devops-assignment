from flask import jsonify, request
from pydash import omit

from .. import routes
from api.middleware import db, auth
from api.models import User


@routes.route('/auth/register', methods=['POST'])
def register():
  body = request.get_json()

  user = User(
    username = body['username'],
    hashed_password = auth.hash_password(body['password']),
    name = body['name'],
    email = body['email']
  )
  
  db.session.add(user)
  db.session.commit()

  return { 'access_token': auth.encode_jwt_token(user) }
