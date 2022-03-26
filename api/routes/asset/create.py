import flask

from .. import routes
from api.middleware import db
from api.models import AssetType, Asset


@routes.route('/asset', methods=['POST'])
def create_asset():
  body = flask.request.get_json()

  asset_type_id = body['asset_type_id']
  asset_type = db.session.get(AssetType, asset_type_id)

  asset = Asset(asset_type)

  db.session.add(asset)
  db.session.commit()
  
  return {
    **asset.to_dict(),
    'asset_type': asset.asset_type.to_dict(),
    'user': None if asset.user is None else asset.user.to_dict(),
  }
