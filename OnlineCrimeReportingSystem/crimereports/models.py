from django.db import models
from user.models import GenUser

# Create your models here.

class Crimereports(models.Model):
    user = models.ForeignKey(GenUser, on_delete=models.CASCADE, db_column="User ID")
    # nid = models.IntegerField(db_column= 'NID', unique=True)
    crime_id = models.IntegerField(db_column= 'Crime ID', unique=True)
    location_of_crime = models.TextField(db_column= 'Location of Crime')
    type_of_crime = models.CharField(max_length=50,db_column= 'Type of Crime')
    date_of_crime = models.CharField(max_length=10, db_column= 'Date of Crime')
    crime_description = models.TextField(db_column="Crime Description")