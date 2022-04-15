from uuid import uuid4
from sqlalchemy import (
  Column,
  ForeignKey,
  Integer,
  String,
  Enum
)
from sqlalchemy.orm import relationship

from . import Base
from .enum.asset_request_status import AssetRequestStatus


class AssetRequest(*Base):
  __tablename__ = 'AssetRequest'

  asset_request_id = Column('asset_request_id', Integer, primary_key=True)
  asset_type_id = Column('asset_type_id', ForeignKey('AssetType.asset_type_id'), nullable=False)
  user_id = Column('user_id', ForeignKey('User.user_id'), nullable=False)
  notes = Column('notes', String(1000), nullable=False, default='')
  status = Column('status', Enum(*AssetRequestStatus._asdict().values(), name='AssetRequestStatus'), nullable=False, default='Initiated')

  asset_type = relationship('AssetType', back_populates='asset_requests')
  user = relationship('User', back_populates='requests')

  def __init__(self, asset_type, user, notes):
    self.asset_type = asset_type
    self.user = user
    self.notes = notes
