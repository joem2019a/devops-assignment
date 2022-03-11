from flask import Blueprint
routes = Blueprint('routes', __name__)

from .user.create import *
from .user.read import *
from .user.update import *
from .user.delete import *

from .asset_type.create import *
from .asset_type.read import *
from .asset_type.delete import *

from .asset.create import *
from .asset.delete import *
from .asset.read import *
from .asset.update import *

from .asset_request.create import *
from .asset_request.delete import *
from .asset_request.read import *
from .asset_request.update import *
