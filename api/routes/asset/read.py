from flask import request, jsonify
from flask_praetorian import roles_required, current_user, PraetorianError
from pydash import map_, omit

from .. import routes
from middleware import db
from models import Asset


@routes.route('/api/assets', methods=['GET'])
@roles_required('active_user')
def read_assets():

  requesting_user = current_user()

  as_admin = request.args.get('admin', False, type=bool)
  if as_admin == True:
    if requesting_user.is_admin != True:
      raise PraetorianError('Unauthorised')

  assets = db.session.query(Asset).all() \
            if as_admin == True \
            else db.session.query(Asset).where(
                Asset.user_id == requesting_user.user_id
              ).all()

  return jsonify(map_(
    assets,
    lambda x: {
      **x.to_dict(),
      'asset_type': x.asset_type.to_dict(),
      'user': None if x.user is None else omit(x.user.to_dict(), 'hashed_password'),
    }
  ))


@routes.route('/api/asset/<asset_id>', methods=['GET'])
@roles_required('active_user')
def read_asset(asset_id):
  asset = db.session.get(Asset, asset_id)

  requesting_user = current_user()

  if asset.user is not None:
    if not requesting_user.is_admin:
      if requesting_user.user_id != asset.user.user_id:
        raise PraetorianError('Unauthorised')

  return {
    **asset.to_dict(),
    'asset_type': asset.asset_type.to_dict(),
    'user': None if asset.user is None else omit(asset.user.to_dict(), 'hashed_password'),
  }
