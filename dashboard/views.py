from django.shortcuts import render
from booths.models import Booth
from visits.models import VisitBooking
from payments.models import Payment

def dashboard_home(request):
    user = request.user
    booth_count = Booth.objects.filter(user=user).count()
    visit_count = VisitBooking.objects.filter(email=user.email).count()
    payment_total = Payment.objects.filter(full_name__icontains=user.get_full_name()).count()

    context = {
        'booth_count': booth_count,
        'visit_count': visit_count,
        'payment_total': payment_total,
    }
    return render(request, 'dashboard/dashboard_home.html', context)
