from django import forms
from .models import VisitBooking

class VisitBookingForm(forms.ModelForm):
    class Meta:
        model = VisitBooking
        fields = '__all__'
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
        }
