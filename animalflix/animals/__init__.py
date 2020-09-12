from flask import Blueprint
from .animal import Animal
from .species import Species

api_v1 = Blueprint("animals", __name__)

from . import controller
