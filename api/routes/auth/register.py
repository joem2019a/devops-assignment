from flask import jsonify, request
from pydash import omit

from .. import routes
from middleware import db, auth
from models import User


@routes.route('/api/auth/register', methods=['POST'])
def register():
  body = request.get_json()

  user = User(
    username = body['username'],
    hashed_password = auth.hash_password(body['password']),
    name = body['name'],
    email = body['email'],
    is_admin = 'admin' in body['username']
  )
  
  assert db.session.query(User).where(User.username == body['username']).first() == None

  db.session.add(user)
  db.session.commit()

  return { 
    'access_token': auth.encode_jwt_token(
      user,
      username=user.username,
      email=user.email,
      name=user.name,
      isAdmin=user.is_admin,
    ) 
  }
