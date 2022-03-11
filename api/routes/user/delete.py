from .. import routes
from api.services.db import with_db
from api.models import User


@routes.route('/user/<user_id>', methods=['DELETE'])
@with_db
def delete_user(user_id, conn=None):
  user = conn.get(User, user_id)
  conn.delete(user)
  conn.commit()

  return { 'success': True }
