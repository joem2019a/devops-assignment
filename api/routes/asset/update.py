import flask

from .. import routes
from api.services.db import with_db
from api.models import User, Asset


requesting_user_id = 1 # todo: get this from auth


@routes.route('/asset/<asset_id>', methods=['PUT'])
@with_db
def change_asset_user(asset_id, conn=None):

  requesting_user = conn.get(User, requesting_user_id)
  if requesting_user.is_admin != True: raise Exception()

  asset = conn.get(Asset, asset_id)

  body = flask.request.get_json()
  user_id = body['user_id']
  asset.user = None if user_id is None else conn.get(User, user_id)
  conn.commit()

  return {
    **asset.to_dict(),
    'asset_type': asset.asset_type.to_dict(),
    'user': None if asset.user is None else asset.user.to_dict(),
  }
