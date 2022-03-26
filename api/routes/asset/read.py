from pydash import map_
from flask import jsonify

from .. import routes
from api.middleware import db
from api.models import Asset, User


user_id = 1 # todo - get this from auth


@routes.route('/assets', methods=['GET'])
def read_assets():

  user = db.session.get(User, user_id)
  assets = db.session.query(Asset).all() if user.is_admin == True else db.session.query(Asset).where(Asset.user_id == user_id).all()

  return jsonify(map_(
    assets,
    lambda x: {
      **x.to_dict(),
      'asset_type': x.asset_type.to_dict(),
      'user': None if x.user is None else x.user.to_dict(),
    }
  ))


@routes.route('/asset/<asset_id>', methods=['GET'])
def read_asset(asset_id):
  asset = db.session.get(Asset, asset_id)

  if asset.user is not None and (asset.user.user_id != user_id or asset.user.is_admin != True):
    raise Exception()

  return {
    **asset.to_dict(),
    'asset_type': asset.asset_type.to_dict(),
    'user': None if asset.user is None else asset.user.to_dict(),
  }
