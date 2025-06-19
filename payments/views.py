from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment
import uuid

def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.transaction_id = str(uuid.uuid4())[:12]  # Simulated transaction ID
            payment.is_successful = True  # In real life, validate via API
            payment.save()
            return redirect('payment-success')
    else:
        form = PaymentForm()
    return render(request, 'payments/make_payment.html', {'form': form})

def payment_success(request): 
    return render(request, 'payments/payment_success.html')
