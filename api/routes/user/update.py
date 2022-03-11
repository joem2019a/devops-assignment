import flask

from .. import routes
from api.services.db import with_db
from api.models import User


@routes.route('/user', methods=['PUT'])
@with_db
def update_user(conn=None):
  user = conn.get(User, user_id)

  return user.to_dict()
