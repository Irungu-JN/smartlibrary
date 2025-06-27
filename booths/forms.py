from django import forms
from .models import Booth, BOOTH_NUMBER_CHOICES
from django.utils import timezone

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

        # Set default booth choices to all 20
        self.fields['booth_number'].choices = BOOTH_NUMBER_CHOICES

        # Pre-highlight today's date
        self.fields['date'].initial = timezone.now().date()

        # Optionally disable past dates
        self.fields['date'].widget.attrs['min'] = timezone.now().date().isoformat()

        # Optional: add placeholders
        self.fields['booth_type'].empty_label = "Select Booth Type"
        self.fields['booth_number'].empty_label = "Select Booth Number"
        self.fields['floor'].empty_label = "Select Floor"
        self.fields['time_slot'].empty_label = "Select Time Slot"

    def clean(self):
        cleaned_data = super().clean()
        booth_number = cleaned_data.get('booth_number')
        date = cleaned_data.get('date')
        time_slot = cleaned_data.get('time_slot')

        if booth_number and date and time_slot:
            # Check if booth is already booked at that time
            existing = Booth.objects.filter(
                booth_number=booth_number,
                date=date,
                time_slot=time_slot
            ).exists()

            if existing:
                raise forms.ValidationError(
                    f"🚫 Booth {booth_number} is already booked for {date} at {time_slot}."
                )
        return cleaned_data
