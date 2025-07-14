from django.contrib import admin
from .models import Booth
from django.utils.html import format_html
from django.utils.timezone import localtime


@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'booth_number',
        'booth_type',
        'floor',
        'date',
        'time_slot',
        'status_badge',
        'user_display',
    )
    list_filter = (
        'booth_type',
        'floor',
        'time_slot',
        'is_available',
        'date',
    )
    search_fields = (
        'full_name',
        'booth_number',
        'user__username',
    )
    list_editable = (
        'booth_type',
        'floor',
        'date',
        'time_slot',
    )
    ordering = ('-date', 'time_slot')

    readonly_fields = ('is_available', 'user')

    def status_badge(self, obj):
        color = 'green' if obj.is_available else 'red'
        label = 'Available' if obj.is_available else 'Booked'
        return format_html(
            f'<span style="color:{color}; font-weight:bold;">{label}</span>'
        )
    status_badge.short_description = 'Status'

    def user_display(self, obj):
        if obj.user:
            return f"{obj.user.username}"
        return "-"
    user_display.short_description = "Booked By"

    # Optional admin action
    actions = ["mark_as_available"]

    def mark_as_available(self, request, queryset):
        updated = queryset.update(is_available=True, user=None)
        self.message_user(request, f"{updated} booths marked as available.")
    mark_as_available.short_description = "✅ Mark selected booths as available"
