from sqlalchemy import (
  Column,
  Integer,
  ForeignKey
)
from sqlalchemy.orm import relationship

from . import Base


class Asset(*Base):
  __tablename__ = 'asset'

  asset_id = Column('asset_id', Integer, primary_key=True)
  asset_type_id = Column('asset_type_id', ForeignKey('assettype.asset_type_id'), nullable=False)
  user_id = Column('user_id', ForeignKey('user.user_id')) # nullable as null will signify asset availability

  asset_type = relationship('AssetType', back_populates='assets')
  user = relationship('User', back_populates='assets')


  def __init__(self, asset_type):
    self.asset_type = asset_type

