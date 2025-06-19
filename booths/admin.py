from django.contrib import admin
from .models import Booth

@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'booth_type', 'date', 'time_slot', 'floor', 'booth_number', 'is_available')
    list_filter = ('booth_type', 'floor', 'time_slot', 'is_available', 'date')
    search_fields = ('full_name',)


# Register your models here.
