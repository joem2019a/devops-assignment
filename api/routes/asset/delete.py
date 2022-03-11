from .. import routes
from api.services.db import with_db
from api.models import Asset


@routes.route('/asset/<asset_id>', methods=['DELETE'])
@with_db
def delete_asset(asset_id, conn=None):
  asset = conn.get(Asset, asset_id)

  if asset.user is not None and (asset.user.user_id != user_id or asset.user.is_admin != True):
    raise Exception()
  
  conn.delete(asset)
  conn.commit()

  return { 'success': True }
