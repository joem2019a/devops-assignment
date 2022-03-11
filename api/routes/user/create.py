import flask

from .. import routes
from api.services.db import with_db
from api.models import User


@routes.route('/user', methods=['POST'])
@with_db
def create_user(conn=None):
  body = flask.request.get_json()

  user = User(body['name'], body['email'])
  
  conn.add(user)
  conn.commit()

  return user.to_dict()
