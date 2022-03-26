from .. import routes
from api.middleware import db
from api.models import User


@routes.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
  user = db.session.get(User, user_id)
  db.session.delete(user)
  db.session.commit()

  return { 'success': True }
