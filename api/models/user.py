from sqlalchemy import (
  Column,
  Integer,
  String,
  Boolean,
  ForeignKey
)
from sqlalchemy.orm import relationship

from . import Base


class User(*Base):
  __tablename__ = 'User'

  user_id = Column('user_id', Integer, primary_key=True)
  name = Column('name', String(100), nullable=False)
  email = Column('email', String(100), nullable=False)
  is_admin = Column('is_admin', Boolean, nullable=False, default=False)

  requests = relationship('AssetRequest', back_populates='user')
  assets = relationship('Asset', back_populates='user')

  def __init__(self, name, email):
    self.name = name
    self.email = email
  