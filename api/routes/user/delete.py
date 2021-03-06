from flask_praetorian import roles_required, current_user

from .. import routes
from middleware import db
from models import User


@routes.route('/api/user/<user_id>', methods=['DELETE'])
@roles_required('active_user', 'admin')
def delete_user(user_id):
  user = db.session.get(User, user_id)
  db.session.delete(user)
  db.session.commit()

  return { 'success': True }
