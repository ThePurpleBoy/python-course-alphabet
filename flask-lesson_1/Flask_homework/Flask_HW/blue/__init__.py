from flask import Blueprint
from flask_restful import Api
from blue.main import Main
from blue.fruits import Fruits
from blue.vegetables import Vegetables
from blue.dont_click import DontClick


blue = Blueprint('blue', __name__)
api = Api(blue)

api.add_resource(Main, "/")
api.add_resource(Fruits, "/fruits", '/fruits/update/<string:value>')
api.add_resource(Vegetables, "/vegetables", '/vegetables/update/<string:value>')
api.add_resource(DontClick, "/dont_click")

