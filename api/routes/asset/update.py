import flask

from .. import routes
from api.middleware import db
from api.models import User, Asset


requesting_user_id = 1 # todo: get this from auth


@routes.route('/asset/<asset_id>', methods=['PUT'])
def change_asset_user(asset_id):

  requesting_user = db.session.get(User, requesting_user_id)
  if requesting_user.is_admin != True: raise Exception()

  asset = db.session.get(Asset, asset_id)

  body = flask.request.get_json()
  user_id = body['user_id']
  asset.user = None if user_id is None else db.session.get(User, user_id)
  db.session.commit()

  return {
    **asset.to_dict(),
    'asset_type': asset.asset_type.to_dict(),
    'user': None if asset.user is None else asset.user.to_dict(),
  }
