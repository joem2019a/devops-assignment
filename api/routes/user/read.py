from .. import routes
from api.services.db import with_db
from api.models import User


@routes.route('/user/<user_id>', methods=['GET'])
@with_db
def read_user(user_id, conn=None):
  user = conn.get(User, user_id)

  return user.to_dict()
