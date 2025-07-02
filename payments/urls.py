from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_payment, name='make-payment'),
    path('pay/', views.make_payment, name='make-payment'),
    path('success/', views.payment_success, name='payment-success'),
    path('stk-status/', views.stk_status_view, name='stk_status'),
]
