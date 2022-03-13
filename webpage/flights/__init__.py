from flask import (Blueprint, )

flights_bp = Blueprint('flights', __name__, url_prefix='/flights')

from .index import show_index
from .add import add_flight
from .flight import get_flight

