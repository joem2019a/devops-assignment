import flask

from .. import routes
from api.middleware import db
from api.models import User, AssetRequest


requesting_user_id = 1 # todo: get this from auth


@routes.route('/asset-request/<asset_request_id>', methods=['PUT'])
def update_asset_request(asset_request_id):

  requesting_user = db.session.get(User, requesting_user_id)
  if requesting_user.is_admin != True: raise Exception()

  asset_request = db.session.get(AssetRequest, asset_request_id)

  body = flask.request.get_json()

  if 'status' in body:
    asset_request.status = body['status']

  if 'notes' in body:
    asset_request.notes = body['notes']

  db.session.commit()

  return asset_request.to_dict()
