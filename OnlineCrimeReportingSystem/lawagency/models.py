from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LawAgency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column="User ID")
    agency_ID = models.CharField(max_length=10, db_column="Agency ID", unique=True)
    agency_branch = models.CharField(max_length=10,db_column="Agency Branch")
    usertype = models.CharField(max_length=15, db_column="User Type", default='Law Agency')
    # profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pictures',db_column="Profile Picture")


