from pydash import map_, filter_
from sqlalchemy.orm import class_mapper

from api.middleware import db


def load_join_data(data, nested_relationships={}):
  if data.__class__ == InstrumentedList:
    return map_(data, lambda item: load_join_data(item, nested_relationships))
  else:
    return data.to_dict(include_relationships=nested_relationships) 


class ModelUtils:

  def to_dict(self, include_relationships={}):
    mapper = class_mapper(self.__class__)
    column_names = self.__table__.columns.keys()
    relationships_to_load = include_relationships.keys()
    foregin_key_names = map_(list(self.__table__.foreign_keys), lambda obj: obj.column.name)

    result =  dict([
      *map_(
        filter_(column_names, lambda name: name not in foregin_key_names),
        lambda column_name: (column_name, getattr(self, column_name))
      ),
      *map_(
        relationships_to_load,
        lambda relationship_name: (
          relationship_name, 
          load_join_data(
            getattr(self, relationship_name), 
            nested_relationships=include_relationships[relationship_name]
          )
        )
      )
    ])
    return result

Base = [db.Model, ModelUtils]

from .user import User
from .asset import Asset
from .asset_type import AssetType
from .asset_request import AssetRequest
