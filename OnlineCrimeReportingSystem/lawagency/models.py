from django.db import models

# Create your models here.

class LawAgency(models.Model):
    user_id = models.IntegerField(db_column="User ID")
    name = models.TextField(db_column="Name")
    email = models.TextField(db_column="Email Address")
    agency_branch = models.CharField(max_length=10,db_column="Agency Branch")
    password = models.CharField(max_length=15, db_column="Password")
    class Meta:
        unique_together = ('user_id', 'email')


