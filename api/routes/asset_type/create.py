import flask

from .. import routes
from api.middleware import db
from api.models import AssetType


@routes.route('/asset-type', methods=['POST'])
def create_asset_type():
  body = flask.request.get_json()

  asset_type = AssetType(body['name'], body['description'], body['cost'])
  
  db.session.add(asset_type)
  db.session.commit()

  return asset_type.to_dict()
