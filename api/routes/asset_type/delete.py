from flask_praetorian import roles_required

from .. import routes
from api.middleware import db
from api.models import AssetType


@routes.route('/api/asset-type/<asset_type_id>', methods=['DELETE'])
@roles_required('active_user', 'admin')
def delete_asset_type(asset_type_id):
  asset_type = db.session.get(AssetType, asset_type_id)
  db.session.delete(asset_type)
  db.session.commit()

  return { 'success': True }
