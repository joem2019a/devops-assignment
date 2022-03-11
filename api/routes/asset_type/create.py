import flask

from .. import routes
from api.services.db import with_db
from api.models import AssetType


@routes.route('/asset-type', methods=['POST'])
@with_db
def create_asset_type(conn=None):
  body = flask.request.get_json()

  asset_type = AssetType(body['name'], body['description'], body['cost'])
  
  conn.add(asset_type)
  conn.commit()

  return asset_type.to_dict()
