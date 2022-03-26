from .. import routes
from api.middleware import db
from api.models import AssetRequest


@routes.route('/asset-request/<asset_request_id>', methods=['DELETE'])
def delete_asset_request(asset_request_id):
  asset_request = db.session.get(AssetRequest, asset_request_id)

  if asset.user is not None and (asset.user.user_id != user_id or asset.user.is_admin != True):
    raise Exception()

  db.session.delete(asset_request)
  db.session.commit()

  return { 'success': True }
