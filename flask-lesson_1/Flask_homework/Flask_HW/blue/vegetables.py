from flask import render_template, make_response, abort
from flask_restful import Resource
import json

with open("database/DB_Vegetables.json", 'r') as file:
    vegetables = json.load(file)


class Vegetables(Resource):

    def get(self):
        return make_response(render_template('vegetables.html', list_vegetables=vegetables))

    def post(self, value):
        vegetables.append(value)
        with open("database/DB_Vegetables.json", 'w') as file:
            json.dump(vegetables, file)

    def delete(self, value):
        try:
            vegetables.remove(value)
            with open("database/DB_Vegetables.json", 'w') as file:
                json.dump(vegetables, file)
        except ValueError:
            abort(404, "The product you wanted to delete is not listed here")