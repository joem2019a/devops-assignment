from .. import routes
from api.services.db import with_db
from api.models import AssetRequest


@routes.route('/asset-request/<asset_request_id>', methods=['DELETE'])
@with_db
def delete_asset_request(asset_request_id, conn=None):
  asset_request = conn.get(AssetRequest, asset_request_id)

  if asset.user is not None and (asset.user.user_id != user_id or asset.user.is_admin != True):
    raise Exception()

  conn.delete(asset_request)
  conn.commit()

  return { 'success': True }
