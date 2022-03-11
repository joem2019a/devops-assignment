import flask

from .. import routes
from api.services.db import with_db
from api.models import AssetType, AssetRequest, User


requesting_user_id = 1 # todo: get this from auth


@routes.route('/asset-request', methods=['POST'])
@with_db
def create_asset_request(conn=None):
  body = flask.request.get_json()

  notes = body['notes'] if 'notes' in body else ''
  asset_type_id = body['asset_type_id']
  asset_type = conn.get(AssetType, asset_type_id)
  requesting_user = conn.get(User, requesting_user_id)

  asset_request = AssetRequest(asset_type, requesting_user, notes)

  conn.add(asset_request)
  conn.commit()
  
  return {
    **asset_request.to_dict(),
    'asset_type': asset_request.asset_type.to_dict(),
    'user': asset_request.user.user_id,
  }
