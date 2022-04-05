import flask

from .. import routes
from api.middleware import db
from api.models import User


requesting_user_id = 1 # todo: get this from auth


@routes.route('/user/<user_id>/admin', methods=['POST'])
def change_user_admin_status(user_id):

  requesting_user = db.session.get(User, requesting_user_id)
  if requesting_user.is_admin != True: raise Exception()

  user = db.session.get(User, user_id)

  body = flask.request.get_json()
  is_admin = body['is_admin']

  user.is_admin = True
  db.session.commit()

  return omit(user.to_dict(), 'hashed_password')

