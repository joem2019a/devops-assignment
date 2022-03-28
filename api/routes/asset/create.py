from flask import request
from flask_praetorian import roles_required

from .. import routes
from api.middleware import db
from api.models import AssetType, Asset


@routes.route('/asset', methods=['POST'])
@roles_required('active_user', 'admin')
def create_asset():
  body = request.get_json()

  asset_type_id = body['asset_type_id']
  asset_type = db.session.get(AssetType, asset_type_id)

  asset = Asset(asset_type)

  db.session.add(asset)
  db.session.commit()
  
  return {
    **asset.to_dict(),
    'asset_type': asset.asset_type.to_dict(),
    'user': None,
  }
