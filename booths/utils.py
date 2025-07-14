# booths/utils.py

from datetime import datetime, timedelta
from django.utils.timezone import now
from .models import Booth

def refresh_booth_availability():
    """
    Frees up booths whose time slot has already passed today.
    Marks them as available for future booking.
    """
    current_time = now()
    today = current_time.date()

    # Map each time slot to a cutoff end time
    time_slot_end_map = {
        '08:00 - 10:00': datetime.combine(today, datetime.strptime("10:00", "%H:%M").time()),
        '10:00 - 12:00': datetime.combine(today, datetime.strptime("12:00", "%H:%M").time()),
        '12:00 - 14:00': datetime.combine(today, datetime.strptime("14:00", "%H:%M").time()),
        '14:00 - 16:00': datetime.combine(today, datetime.strptime("16:00", "%H:%M").time()),
        '16:00 - 18:00': datetime.combine(today, datetime.strptime("18:00", "%H:%M").time()),
    }

    booths_to_free = Booth.objects.filter(is_available=False, date=today)

    freed_count = 0
    for booth in booths_to_free:
        end_time = time_slot_end_map.get(booth.time_slot)
        if end_time and current_time > end_time:
            booth.is_available = True
            booth.user = None
            booth.save()
            freed_count += 1

    return freed_count
