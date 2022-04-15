from flask_praetorian import roles_required, current_user, PraetorianError

from .. import routes
from middleware import db
from models import AssetRequest


@routes.route('/api/asset-request/<asset_request_id>', methods=['DELETE'])
@roles_required('active_user')
def delete_asset_request(asset_request_id):

  requesting_user = current_user()

  asset_request = db.session.get(AssetRequest, asset_request_id)

  if not requesting_user.is_admin:
    if requesting_user.user_id != asset_request.user_id:
      raise PraetorianError('Unauthorised')

  db.session.delete(asset_request)
  db.session.commit()

  return { 'success': True }
