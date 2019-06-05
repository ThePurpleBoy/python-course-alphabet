from flask import render_template, make_response
from flask_restful import Resource


class DontClick(Resource):

    def get(self):
        return make_response(render_template('dont_click.html'))