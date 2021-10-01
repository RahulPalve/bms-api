import logging
from flask import request
from flask_restful import Resource
from bms.models import Show

class Movies(Resource):
    def get(self, **kwargs):
        try:
            movies = Show.objects.filter(
                cinema__city__name=kwargs["city_name"]
                ).distinct(field="movie").values_list("movie")
            return movies.to_json()

        except Show.DoesNotExist:
            return {"status": "error", "msg": "No Movies/Shows found in this city"}
