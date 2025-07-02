from django.db import models

# Create your models here
# users/models.py
from django.contrib.auth.models import User
from django.db import models

class UserVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    visit_date = models.DateField()
    group_size = models.IntegerField()
    # and any other fields
