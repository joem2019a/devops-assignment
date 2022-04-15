from sqlalchemy import (
  Column,
  Integer,
  String,
  Text,
  Boolean,
)
from sqlalchemy.orm import relationship

from . import Base


class User(*Base):
  __tablename__ = 'User'
  __tableargs__ = { "extend_existing": True }

  user_id = Column('user_id', Integer, primary_key=True)
  username = Column('username', String(10), nullable=False)
  hashed_password = Column('hashed_password', Text, nullable=False)
  name = Column('name', String(100), nullable=False)
  email = Column('email', String(100), nullable=False)
  is_admin = Column('is_admin', Boolean, nullable=False, default=False)
  is_enabled = Column('is_enabled', Boolean, default=True)

  requests = relationship('AssetRequest', back_populates='user')
  assets = relationship('Asset', back_populates='user')
  
  @property
  def identity(self):
    return self.user_id

  @property
  def rolenames(self):

    roles = []

    if self.is_admin == True: roles.append('admin')
    if self.is_enabled == True: roles.append('active_user')

    return roles

  @property
  def password(self):
    return self.hashed_password

  @classmethod
  def lookup(cls, username):
    return cls.query.filter_by(username=username).one_or_none()

  @classmethod
  def identify(cls, id):
    return cls.query.get(id)
