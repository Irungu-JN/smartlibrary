from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='booths-home'),
    path('book/', views.book_booth, name='booths-book'),
    path('confirmation/', views.booking_confirmation, name='booths-confirmation'),
]
