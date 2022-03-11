from .. import routes
from api.services.db import with_db
from api.models import AssetType


@routes.route('/asset-type/<asset_type_id>', methods=['DELETE'])
@with_db
def delete_asset_type(asset_type_id, conn=None):
  asset_type = conn.get(AssetType, asset_type_id)
  conn.delete(asset_type)
  conn.commit()

  return { 'success': True }
