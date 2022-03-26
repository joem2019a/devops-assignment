import flask
from pendulum import duration

from api.middleware import auth, cors, db
from api.routes import routes
from api.models import User
from api.utils import jti_blacklist

def create_app(*args, **kwargs):
  app = flask.Flask(__name__)

  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.config["SECRET_KEY"] = "top secret"
  app.config["JWT_ACCESS_LIFESPAN"] = duration(hours=24)
  app.config["JWT_REFRESH_LIFESPAN"] = duration(days=30)

  auth.init_app(app, User, is_blacklisted=jti_blacklist.is_blacklisted)

  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///assetmanager.sqlite"
  
  db.init_app(app)
  cors.init_app(app)

  app.register_blueprint(routes)
  
  with app.app_context():
    db.create_all()

  return app
