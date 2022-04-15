from flask import request, jsonify
from flask_praetorian import roles_required, current_user, PraetorianError
from pydash import map_, omit

from .. import routes
from middleware import db
from models import AssetRequest


@routes.route('/api/asset-requests', methods=['GET'])
@roles_required('active_user')
def read_asset_requests():
  requesting_user = current_user()
  requesting_user_id = requesting_user.user_id

  as_admin = request.args.get('admin', False, type=bool)
  if as_admin == True:
    if requesting_user.is_admin != True:
      raise PraetorianError('Unauthorised')

  asset_requests = db.session.query(AssetRequest).all() \
                    if as_admin == True \
                    else db.session.query(AssetRequest).where(
                        AssetRequest.user_id == requesting_user_id
                      ).all()

  return jsonify(map_(
    asset_requests,
    lambda x: {
      **x.to_dict(),
      'asset_type': x.asset_type.to_dict(),
      'user': None if x.user is None else omit(x.user.to_dict(), 'hashed_password'),
    }
  ))


@routes.route('/api/asset-request/<asset_request_id>', methods=['GET'])
@roles_required('active_user')
def read_asset_request(asset_request_id):
  requesting_user = current_user()

  asset_request = db.session.get(AssetRequest, asset_request_id)

  if not requesting_user.is_admin:
    if requesting_user.user_id != asset_request.user_id:
      raise PraetorianError('Unauthorised')

  return {
    **asset_request.to_dict(),
    'asset_type': asset_request.asset_type.to_dict(),
    'user': None if asset_request.user is None else omit(asset_request.user.to_dict(), 'hashed_password'),
  }
