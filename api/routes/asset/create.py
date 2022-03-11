import flask

from .. import routes
from api.services.db import with_db
from api.models import AssetType, Asset


@routes.route('/asset', methods=['POST'])
@with_db
def create_asset(conn=None):
  body = flask.request.get_json()

  asset_type_id = body['asset_type_id']
  asset_type = conn.get(AssetType, asset_type_id)

  asset = Asset(asset_type)

  conn.add(asset)
  conn.commit()
  
  return {
    **asset.to_dict(),
    'asset_type': asset.asset_type.to_dict(),
    'user': None if asset.user is None else asset.user.to_dict(),
  }
