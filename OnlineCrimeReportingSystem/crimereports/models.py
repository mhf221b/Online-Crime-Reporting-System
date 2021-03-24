from django.db import models

# Create your models here.

class Crimereports(models.Model):
    nid = models.IntegerField(db_column= 'NID')
    crime_id =  models.IntegerField(primary_key=True, db_column= 'Crime ID')
    location_of_crime = models.TextField(db_column= 'Location of Crime')
    type_of_crime = models.TextField(db_column= 'Type of Crime')
    date_of_crime = models.CharField(max_length=10, db_column= 'Date of Crime')
