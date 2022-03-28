from flask import request
from flask_praetorian import roles_required
from pydash import omit

from .. import routes
from api.middleware import db
from api.models import User


@routes.route('/user/<user_id>/admin', methods=['POST'])
@roles_required('active_user', 'admin')
def change_user_admin_status(user_id):

  user = db.session.get(User, user_id)

  body = request.get_json()

  user.is_admin = body['is_admin']
  db.session.commit()

  return omit(user.to_dict(), 'hashed_password')

