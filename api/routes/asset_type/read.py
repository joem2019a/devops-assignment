from pydash import map_
from flask import jsonify

from .. import routes
from api.middleware import db
from api.models import AssetType


@routes.route('/asset-types', methods=['GET'])
def read_asset_types():
  asset_types = db.session.query(AssetType).all()

  return jsonify(map_(
    asset_types,
    lambda x: x.to_dict()
  ))


@routes.route('/asset-type/<asset_type_id>', methods=['GET'])
def read_asset_type(asset_type_id):
  asset_type = db.session.get(AssetType, asset_type_id)

  return asset_type.to_dict()

