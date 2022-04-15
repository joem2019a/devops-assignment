from flask import request
from flask_praetorian import roles_required

from .. import routes
from middleware import db
from models import AssetType


@routes.route('/api/asset-type', methods=['POST'])
@roles_required('active_user', 'admin')
def create_asset_type():
  body = request.get_json()

  asset_type = AssetType(body['name'], body['description'], body['cost'])
  
  db.session.add(asset_type)
  db.session.commit()

  return asset_type.to_dict()
