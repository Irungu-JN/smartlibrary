from django.urls import path
from . import views

urlpatterns = [
    path('', views.visit_list, name='visit-list'),
    path('book/', views.book_visit, name='book-visit'),
    path('thank-you/', views.thank_you, name='visit-thank-you'),
]
