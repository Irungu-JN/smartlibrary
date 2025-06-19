# booths/utils.py
from datetime import datetime
from .models import Booth

def refresh_booth_availability():
    now = datetime.now()
    Booth.objects.filter(is_available=False, booked_until__lt=now).update(is_available=True, user=None, booked_until=None)
