from bms import rest_api
from .views import Movies

rest_api.add_resorce(Movies, "city/<string:city_name>")