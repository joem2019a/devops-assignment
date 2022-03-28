from flask import jsonify
from flask_praetorian import roles_required, current_user, PraetorianError
from pydash import map_, omit

from .. import routes
from api.middleware import db
from api.models import Asset


@routes.route('/assets', methods=['GET'])
@roles_required('active_user')
def read_assets():

  requesting_user = current_user()

  assets = db.session.query(Asset).all() \
            if requesting_user.is_admin == True \
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


@routes.route('/asset/<asset_id>', methods=['GET'])
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
