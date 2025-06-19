from django.db import models
from django.contrib.auth.models import User

class VisitBooking(models.Model):
    school_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    visit_date = models.DateField()
    group_size = models.PositiveIntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.school_name} - {self.visit_date}"


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    visit_date = models.DateField()
    group_size = models.IntegerField()
    # other fields...
