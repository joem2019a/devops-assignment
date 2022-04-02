from flask import request
from flask_praetorian import roles_required
from pydash import omit

from .. import routes
from api.middleware import db
from api.models import User, Asset


@routes.route('/api/asset/<asset_id>', methods=['PUT'])
@roles_required('active_user', 'admin')
def change_asset_user(asset_id):

  asset = db.session.get(Asset, asset_id)

  body = request.get_json()
  user_id = body['user_id']
  asset.user = None if user_id is None else db.session.get(User, user_id)
  db.session.commit()

  return {
    **asset.to_dict(),
    'asset_type': asset.asset_type.to_dict(),
    'user': None if asset.user is None else omit(asset.user.to_dict(), 'hashed_password'),
  }
