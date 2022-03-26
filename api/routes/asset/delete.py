from .. import routes
from api.middleware import db
from api.models import Asset


@routes.route('/asset/<asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
  asset = db.session.get(Asset, asset_id)

  if asset.user is not None and (asset.user.user_id != user_id or asset.user.is_admin != True):
    raise Exception()
  
  db.session.delete(asset)
  db.session.commit()

  return { 'success': True }
