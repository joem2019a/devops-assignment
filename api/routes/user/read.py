from pydash import omit

from .. import routes
from api.middleware import db
from api.models import User


@routes.route('/user/<user_id>', methods=['GET'])
def read_user(user_id):
  user = db.session.get(User, user_id)

  return omit(user.to_dict(), 'hashed_password')

