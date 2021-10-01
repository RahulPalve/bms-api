import datetime, uuid
from bms import db

class City(db.Document):
    name = db.StringField(required=True)
    
class Cinema(db.Document):
    name = db.StringField(required=True)
    city = db.ReferenceField(City)

class Movie(db.Document):
    name = db.StringField()
    rating = db.IntField(default=5)

class Show(db.Document):
    name = db.StringField()
    start_time = db.DateTimeField(default=datetime.datetime.now)
    end_time = db.DateTimeField(default=datetime.datetime.now)
    total_seats = db.IntField(default=20)
    available_seats = db.IntField(default=20)
    cinema = db.ReferenceField(Cinema)  
    movie = db.ReferenceField(Movie)



