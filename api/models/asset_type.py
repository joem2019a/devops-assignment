from sqlalchemy import (
  Column,
  String,
  Integer,
)
from sqlalchemy.orm import relationship

from . import Base


class AssetType(*Base):
  __tablename__ = 'AssetType'

  asset_type_id = Column('asset_type_id', Integer, primary_key=True)
  name = Column('name', String(255), nullable=False)
  description = Column('description', String(1000), nullable=False)
  cost = Column('cost', Integer, nullable=False) # will be stored in pennies, hence integer

  assets = relationship('Asset', back_populates='asset_type')
  asset_requests = relationship('AssetRequest', back_populates='asset_type')

  def __init__(self, name, description, cost):
    self.name = name
    self.description = description
    self.cost = cost
