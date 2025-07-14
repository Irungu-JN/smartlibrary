from django.db import models
from django.contrib.auth.models import User

BOOTH_NUMBER_CHOICES = [(i, f'Booth {i}') for i in range(1, 21)]  # Global constant

class Booth(models.Model):
    BOOTH_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Group', 'Group'),
    ]

    FLOOR_CHOICES = [
        ('First Floor', 'First Floor'),
        ('Second Floor', 'Second Floor'),
        ('Third Floor', 'Third Floor'),
    ]

    TIME_SLOT_CHOICES = [
        ('08:00 - 10:00', '08:00 - 10:00'),
        ('10:00 - 12:00', '10:00 - 12:00'),
        ('12:00 - 14:00', '12:00 - 14:00'),
        ('14:00 - 16:00', '14:00 - 16:00'),
        ('16:00 - 18:00', '16:00 - 18:00'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    booth_type = models.CharField(max_length=10, choices=BOOTH_TYPE_CHOICES)
    date = models.DateField()
    time_slot = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES)
    floor = models.CharField(max_length=20, choices=FLOOR_CHOICES)
    booth_number = models.IntegerField(choices=BOOTH_NUMBER_CHOICES)  # ✅ Correctly here
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.booth_type} - Booth {self.booth_number} ({self.floor})"