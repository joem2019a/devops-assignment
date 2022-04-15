from flask_praetorian import roles_required

from .. import routes
from middleware import db
from models import Asset


@routes.route('/api/asset/<asset_id>', methods=['DELETE'])
@roles_required('active_user', 'admin')
def delete_asset(asset_id):
  asset = db.session.get(Asset, asset_id)
  
  db.session.delete(asset)
  db.session.commit()

  return { 'success': True }
