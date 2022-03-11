from pydash import map_
from json import dumps

from .. import routes
from api.services.db import with_db
from api.models import Asset, User


user_id = 1 # todo - get this from auth


@routes.route('/assets', methods=['GET'])
@with_db
def read_assets(conn=None):

  user = conn.get(User, user_id)
  assets = conn.query(Asset).all() if user.is_admin == True else conn.query(Asset).where(Asset.user_id == user_id).all()

  return dumps(map_(
    assets,
    lambda x: {
      **x.to_dict(),
      'asset_type': x.asset_type.to_dict(),
      'user': None if x.user is None else x.user.to_dict(),
    }
  ))


@routes.route('/asset/<asset_id>', methods=['GET'])
@with_db
def read_asset(asset_id, conn=None):
  asset = conn.get(Asset, asset_id)

  if asset.user is not None and (asset.user.user_id != user_id or asset.user.is_admin != True):
    raise Exception()

  return {
    **asset.to_dict(),
    'asset_type': asset.asset_type.to_dict(),
    'user': None if asset.user is None else asset.user.to_dict(),
  }
