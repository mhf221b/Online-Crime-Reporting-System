from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20, db_column="First Name")
    last_name = models.CharField(max_length=20, db_column="Last Name")
    nid = models.IntegerField(db_column="NID")
    email = models.TextField(db_column="Email Address")
    home_address = models.TextField(db_column="Home Address")
    gender = models.CharField(max_length=10,db_column="Gender")
    mobile_number = models.CharField(max_length=15, db_column="Mobile Number")
    password = models.CharField(max_length=15, db_column="Password")

    class Meta:
        unique_together = ('nid', 'email', 'mobile_number')