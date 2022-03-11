import flask

from api.routes import routes
from .services.db import DatabaseConn

app = flask.Flask(__name__)
app.register_blueprint(routes)


def startflask():
  app.run()


if __name__ == "__main__":
  db = DatabaseConn()
  db.build_schema()
  del db
  startflask()
