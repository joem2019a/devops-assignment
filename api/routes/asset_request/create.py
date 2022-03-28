from flask import request
from flask_praetorian import roles_required, current_user
from pydash import omit

from .. import routes
from api.middleware import db
from api.models import AssetType, AssetRequest


@routes.route('/asset-request', methods=['POST'])
@roles_required('active_user')
def create_asset_request():
  body = request.get_json()
  requesting_user = current_user()

  notes = body['notes'] if 'notes' in body else ''
  asset_type_id = body['asset_type_id']
  asset_type = db.session.get(AssetType, asset_type_id)

  asset_request = AssetRequest(asset_type, requesting_user, notes)

  db.session.add(asset_request)
  db.session.commit()
  
  return {
    **asset_request.to_dict(),
    'asset_type': asset_request.asset_type.to_dict(),
    'user': omit(asset_request.user.to_dict(), 'hashed_password'),
  }
