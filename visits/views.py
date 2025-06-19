
# Create your views here.
from django.shortcuts import render, redirect
from .forms import VisitBookingForm
from .models import VisitBooking

def book_visit(request):
    if request.method == 'POST':
        form = VisitBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit-thank-you')
    else:
        form = VisitBookingForm()
    return render(request, 'visits/book_visit.html', {'form': form})

def visit_list(request):
    visits = VisitBooking.objects.all().order_by('-visit_date')
    return render(request, 'visits/visit_list.html', {'visits': visits})

def thank_you(request):
    return render(request, 'visits/thank_you.html')
