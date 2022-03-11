from flask import Blueprint
routes = Blueprint('routes', __name__)

from .user.create import *
