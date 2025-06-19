from django import forms
from .models import Booth

class BoothBookingForm(forms.ModelForm):
    class Meta:
        model = Booth
        fields = ['booth_type', 'booth_number', 'floor', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'}),
            'booth_number': forms.Select(attrs={'class': 'form-control'}),
            'floor': forms.Select(attrs={'class': 'form-control'}),
            'booth_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Assuming booth_number is a CharField or IntegerField, not a ForeignKey
        available_booths = Booth.objects.filter(is_available=True).values_list('booth_number', flat=True).distinct()
        self.fields['booth_number'].choices = [(num, f'Booth {num}') for num in available_booths]
