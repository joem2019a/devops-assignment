from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.models import BaseModel


class DatabaseConn:

    def __init__(self):

        self._engine = create_engine("sqlite:///assetmanager.sqlite")
        self.session = None


    def build_schema(self):
        if self.session is not None:
            raise Exception()

        BaseModel.metadata.create_all(bind=self._engine)


    def __enter__(self):
        if self.session is not None:
            raise Exception()
        
        Session = sessionmaker(bind=self._engine)
        self.session = Session()

        return self.session


    def __exit__(self, *args):
        if self.session is None:
            raise Exception()

        self.session.close()
        self.session = None


def with_db(function):

    @wraps(function)
    def decorated(*args, **kwargs):
        with DatabaseConn() as conn:
            return function(*args, **kwargs, conn=conn)
        
    return decorated
