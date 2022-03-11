import flask

from .. import routes
from api.services.db import with_db
from api.models import User


requesting_user_id = 1 # todo: get this from auth


@routes.route('/user/<user_id>/admin', methods=['POST'])
@with_db
def change_user_admin_status(user_id, conn=None):

  requesting_user = conn.get(User, requesting_user_id)
  if requesting_user.is_admin != True: raise Exception()

  user = conn.get(User, user_id)

  body = flask.request.get_json()
  is_admin = body['is_admin']

  user.is_admin = True
  conn.commit()

  return user.to_dict()
