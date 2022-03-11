from pydash import map_
from json import dumps

from .. import routes
from api.services.db import with_db
from api.models import AssetType


@routes.route('/asset-types', methods=['GET'])
@with_db
def read_asset_types(conn=None):
  asset_types = conn.query(AssetType).all()

  return dumps(map_(
    asset_types,
    lambda x: x.to_dict()
  ))


@routes.route('/asset-type/<asset_type_id>', methods=['GET'])
@with_db
def read_asset_type(asset_type_id, conn=None):
  asset_type = conn.get(AssetType, asset_type_id)

  return asset_type.to_dict()

