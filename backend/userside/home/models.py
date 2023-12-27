from django.db import models
from .db_connection import db
# Create your models here.


post_collection = db['Posts']

Comments = db['comments'] 

Callouts = db['callouts'] 

Follow = db['Follow'] 