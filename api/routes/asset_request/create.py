import flask

from .. import routes
from api.middleware import db
from api.models import AssetType, AssetRequest, User


requesting_user_id = 1 # todo: get this from auth


@routes.route('/asset-request', methods=['POST'])
def create_asset_request():
  body = flask.request.get_json()

  notes = body['notes'] if 'notes' in body else ''
  asset_type_id = body['asset_type_id']
  asset_type = db.session.get(AssetType, asset_type_id)
  requesting_user = db.session.get(User, requesting_user_id)

  asset_request = AssetRequest(asset_type, requesting_user, notes)

  db.session.add(asset_request)
  db.session.commit()
  
  return {
    **asset_request.to_dict(),
    'asset_type': asset_request.asset_type.to_dict(),
    'user': asset_request.user.user_id,
  }
