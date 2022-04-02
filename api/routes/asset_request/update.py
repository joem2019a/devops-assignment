from flask import request
from flask_praetorian import roles_required, current_user, PraetorianError

from .. import routes
from api.middleware import db
from api.models import AssetRequest


@routes.route('/api/asset-request/<asset_request_id>', methods=['PUT'])
@roles_required('active_user')
def update_asset_request(asset_request_id):

  requesting_user = current_user()

  asset_request = db.session.get(AssetRequest, asset_request_id)

  if not requesting_user.is_admin:
    if requesting_user.user_id != asset_request.user_id:
      raise PraetorianError('Unauthorised')

  body = request.get_json()

  if 'status' in body:
    asset_request.status = body['status']

  if 'notes' in body:
    asset_request.notes = body['notes']

  db.session.commit()

  return asset_request.to_dict()
