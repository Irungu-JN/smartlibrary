from django.db import models
from django.utils import timezone

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('MPESA', 'M-Pesa'),
        ('PAYPAL', 'PayPal'),
        ('CARD', 'Card'),
        ('CASH', 'Cash'),
    ]

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, blank=True)
    paid_on = models.DateTimeField(default=timezone.now)
    is_successful = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.full_name} - {self.amount} ({self.payment_method})"
