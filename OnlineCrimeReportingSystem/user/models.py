from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GenUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column="User ID")
    # first_name = models.CharField(max_length=20, db_column="First Name")
    # last_name = models.CharField(max_length=20, db_column="Last Name")
    nid = models.IntegerField(db_column="NID", unique=True)
    # email = models.TextField(db_column="Email Address")
    home_address = models.TextField(db_column="Home Address")
    gender = models.CharField(max_length=10,db_column="Gender")
    mobile_number = models.CharField(max_length=15, db_column="Mobile Number", unique=True)
    # password = models.CharField(max_length=15, db_column="Password")