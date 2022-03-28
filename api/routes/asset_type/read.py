from flask import jsonify
from flask_praetorian import roles_required
from pydash import map_

from .. import routes
from api.middleware import db
from api.models import AssetType


@routes.route('/asset-types', methods=['GET'])
@roles_required('active_user')
def read_asset_types():
  asset_types = db.session.query(AssetType).all()

  return jsonify(map_(
    asset_types,
    lambda x: x.to_dict()
  ))


@routes.route('/asset-type/<asset_type_id>', methods=['GET'])
@roles_required('active_user')
def read_asset_type(asset_type_id):
  asset_type = db.session.get(AssetType, asset_type_id)

  return asset_type.to_dict()

