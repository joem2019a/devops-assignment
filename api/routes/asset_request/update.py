import flask

from .. import routes
from api.services.db import with_db
from api.models import User, AssetRequest


requesting_user_id = 1 # todo: get this from auth


@routes.route('/asset-request/<asset_request_id>', methods=['PUT'])
@with_db
def update_asset_request(asset_request_id, conn=None):

  requesting_user = conn.get(User, requesting_user_id)
  if requesting_user.is_admin != True: raise Exception()

  asset_request = conn.get(AssetRequest, asset_request_id)

  body = flask.request.get_json()

  if 'status' in body:
    asset_request.status = body['status']

  if 'notes' in body:
    asset_request.notes = body['notes']

  conn.commit()

  return asset_request.to_dict()
