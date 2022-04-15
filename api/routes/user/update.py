from flask import request
from flask_praetorian import roles_required
from pydash import omit

from .. import routes
from middleware import db
from models import User


@routes.route('/api/user/<user_id>/admin', methods=['POST'])
@roles_required('active_user', 'admin')
def change_user_admin_status(user_id):

  user = db.session.get(User, user_id)

  body = request.get_json()
  print(body)

  print(bool(body['is_admin']))
  user.is_admin = body['is_admin']
  db.session.commit()

  return omit(user.to_dict(), 'hashed_password')

