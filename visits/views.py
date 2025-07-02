
# Create your views here.
from django.shortcuts import render, redirect
from .forms import VisitBookingForm
from .models import VisitBooking
from .models import Visit
from django.contrib.auth.decorators import login_required
@login_required
def book_visit(request):
    if request.method == 'POST':
        form = VisitBookingForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.user = request.user  # Associate the visit with the logged-in user
            visit.save()
            return redirect('visit-thank-you')
    else:
        form = VisitBookingForm()
    return render(request, 'visits/book_visit.html', {'form': form})
    

def visit_list(request):
    visits = VisitBooking.objects.all().order_by('-visit_date')
    return render(request, 'visits/visit_list.html', {'visits': visits})

def thank_you(request):
    return render(request, 'visits/thank_you.html')

@login_required
def book_visit(request):
    if request.method == 'POST':
        form = VisitBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # ✅ user is set programmatically
            booking.save()
            return redirect('profile')
    else:
        form = VisitBookingForm()

    return render(request, 'visits/book_visit.html', {'form': form})
