from .. import routes
from api.middleware import db
from api.models import AssetType


@routes.route('/asset-type/<asset_type_id>', methods=['DELETE'])
def delete_asset_type(asset_type_id):
  asset_type = db.session.get(AssetType, asset_type_id)
  db.session.delete(asset_type)
  db.session.commit()

  return { 'success': True }
