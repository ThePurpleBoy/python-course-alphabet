from flask import render_template, make_response, abort
from flask_restful import Resource
import json

with open("database/DB_Fruits.json", 'r') as file:
    fruits = json.load(file)


class Fruits(Resource):

    def get(self):
        return make_response(render_template('fruits.html', list_fruits=fruits))

    def post(self, value):
        fruits.append(value)
        with open("database/DB_Fruits.json", 'w') as file:
            json.dump(fruits, file)

    def delete(self, value):
        try:
            fruits.remove(value)
            with open("database/DB_Fruits.json", 'w') as file:
                json.dump(fruits, file)
        except ValueError:
            abort(404, "The product you wanted to delete is not listed here")

