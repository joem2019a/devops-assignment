from flask import Flask
from os import getenv
from pendulum import duration

from middleware import auth, cors, db
from routes import routes
from models import User
from utils import jti_blacklist


FALLBACK_SECRET_KEY = 'YzdmMmNhYTE3Yzg2ZDg5Yjc0MjM2Y2IzYTQ3OGZlYmY5MTk2MDAwOWRmODhkNDQ0ZjJhNmI0ODM3Mzg1OGY3NA=='


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = getenv('SECRET_KEY', FALLBACK_SECRET_KEY)
app.config["JWT_ACCESS_LIFESPAN"] = duration(hours=24)
app.config["JWT_REFRESH_LIFESPAN"] = duration(days=30)

auth.init_app(app, User, is_blacklisted=jti_blacklist.is_blacklisted)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///assetmanager.sqlite"

db.init_app(app)
cors.init_app(app)

app.register_blueprint(routes)

# with app.app_context():
#   db.create_all()

if __name__ == "__main__":
  app.run('0.0.0.0', 5000, True)