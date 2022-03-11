from pydash import map_
from json import dumps

from .. import routes
from api.services.db import with_db
from api.models import AssetRequest, User


user_id = 1 # todo - get this from auth


@routes.route('/asset-requests', methods=['GET'])
@with_db
def read_asset_requests(conn=None):

  user = conn.get(User, user_id)
  asset_requests = conn.query(AssetRequest).all() if user.is_admin == True else conn.query(AssetRequest).where(AssetRequest.user_id == user_id).all()

  return dumps(map_(
    asset_requests,
    lambda x: {
      **x.to_dict(),
      'asset_type': x.asset_type.to_dict(),
      'user': None if x.user is None else x.user.to_dict(),
    }
  ))


@routes.route('/asset-request/<asset_request_id>', methods=['GET'])
@with_db
def read_asset_request(asset_request_id, conn=None):
  asset_request = conn.get(AssetRequest, asset_request_id)

  if asset_request.user is not None and (asset_request.user.user_id != user_id or asset_request.user.is_admin != True):
    raise Exception()

  return {
    **asset_request.to_dict(),
    'asset_type': asset_request.asset_type.to_dict(),
    'user': None if asset_request.user is None else asset_request.user.to_dict(),
  }
