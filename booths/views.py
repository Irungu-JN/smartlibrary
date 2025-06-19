from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BoothBookingForm
from .models import Booth

def home(request):
    available_booths = Booth.objects.filter(is_available=True).order_by('date', 'time_slot')

    return render(request, 'booths/home.html', {
        'available_booths': available_booths,
        'page_title': 'SmartLibrary – Available Reading Booths'
    })

@login_required
def book_booth(request):
    if request.method == 'POST':
        form = BoothBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booths-confirmation')
    else:
        form = BoothBookingForm()

    return render(request, 'booths/book_booth.html', {
        'form': form,
        'page_title': 'Book a Reading Booth',
        'submit_text': 'Confirm Booking'
    })

@login_required
def booking_confirmation(request):
    return render(request, 'booths/confirmation.html', {
        'message': '🎉 Your booth booking was successful!',
        'page_title': 'Booking Confirmed',
        'next_step': 'Check your profile or book another slot.'
    })
