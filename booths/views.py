from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booth
from .forms import BoothBookingForm
from datetime import date


def home(request):
    """
    Displays all available booths.
    """
    available_booths = Booth.objects.all().order_by('date', 'time_slot', 'booth_number')
     # No need to change template


    return render(request, 'booths/home.html', {
        'available_booths': available_booths,
        'page_title': 'SmartLibrary – Available Reading Booths'
    })


@login_required
def book_booth(request):
    """
    Handles booth booking with validation and pre-fill if booth is passed as a query param.
    """
    initial_data = {}

    # Support pre-filling booth from ?booth=ID
    booth_id = request.GET.get('booth')
    if booth_id and booth_id.isdigit():
        try:
            booth = Booth.objects.get(id=booth_id)
            initial_data['booth_number'] = booth.booth_number
        except Booth.DoesNotExist:
            pass

    if request.method == 'POST':
        form = BoothBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.full_name = request.user.get_full_name() or request.user.username
            booking.is_available = False  # Mark as booked
            booking.save()
            return redirect('booths-confirmation')
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = BoothBookingForm(initial=initial_data)

    return render(request, 'booths/book_booth.html', {
        'form': form,
        'page_title': '📖 Book a Reading Booth',
    })


@login_required
def booking_confirmation(request):
    """
    Shown after a successful booking.
    """
    return render(request, 'booths/confirmation.html', {
        'page_title': '🎉 Booking Confirmed',
    })
