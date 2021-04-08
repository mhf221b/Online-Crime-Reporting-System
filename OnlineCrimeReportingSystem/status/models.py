from django.db import models
from crimereports.models import Crimereports
# Create your models here.

class Status(models.Model):
    user = models.OneToOneField(Crimereports, on_delete=models.CASCADE, db_column="User ID")
    # crime_id = models.OneToOneField(Crimereports, on_delete=models.CASCADE)
    complaint_status = models.CharField(max_length=10, db_column= 'Complaint Status')
    # complaint_history = models.CharField(max_length=10, db_column= 'Complaint History')
    date = models.CharField(max_length=10, db_column= 'Date')