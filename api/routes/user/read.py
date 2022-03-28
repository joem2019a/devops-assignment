from flask import jsonify
from flask_praetorian import roles_required, current_user, PraetorianError
from pydash import omit, map_

from .. import routes
from api.middleware import db
from api.models import User


@routes.route('/user/<user_id>', methods=['GET'])
@roles_required('active_user')
def read_user_by_id(user_id):
  requesting_user = current_user()

  if not requesting_user.is_admin:
    if requesting_user.user_id != user_id:
      raise PraetorianError('Unauthorised')

  user = db.session.get(User, user_id)

  return omit(user.to_dict(), 'hashed_password')


@routes.route('/user', methods=['GET'])
@roles_required('active_user')
def read_user():
  user = current_user()

  return omit(user.to_dict(), 'hashed_password')


@routes.route('/users', methods=['GET'])
@roles_required('active_user', 'admin')
def read_users():
  users = db.session.query(User).all()

  return jsonify(
    map_(
      users, 
      lambda x: omit(x.to_dict(), 'hashed_password')
    )
  )
