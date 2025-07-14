from django import forms
from django.utils import timezone
from .models import Booth, BOOTH_NUMBER_CHOICES


class BoothBookingForm(forms.ModelForm):
    class Meta:
        model = Booth
        fields = ['booth_type', 'booth_number', 'floor', 'date', 'time_slot']
        widgets = {
            'booth_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'booth_number': forms.Select(attrs={
                'class': 'form-control',
            }),
            'floor': forms.Select(attrs={
                'class': 'form-control',
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'time_slot': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        today = timezone.now().date()

        # Set default booth number choices (1–20)
        self.fields['booth_number'].choices = BOOTH_NUMBER_CHOICES

        # Set min selectable date to today
        self.fields['date'].widget.attrs['min'] = today.isoformat()
        self.fields['date'].initial = today

        # Add clean placeholders
        self.fields['booth_type'].empty_label = "📚 Select Booth Type"
        self.fields['booth_number'].empty_label = "🔢 Select Booth Number"
        self.fields['floor'].empty_label = "🏢 Select Floor"
        self.fields['time_slot'].empty_label = "⏰ Select Time Slot"

    def clean(self):
        cleaned_data = super().clean()
        booth_number = cleaned_data.get('booth_number')
        date = cleaned_data.get('date')
        time_slot = cleaned_data.get('time_slot')

        # Prevent double booking
        if booth_number and date and time_slot:
            already_booked = Booth.objects.filter(
                booth_number=booth_number,
                date=date,
                time_slot=time_slot
            ).exists()

            if already_booked:
                raise forms.ValidationError(
                    f"🚫 Booth {booth_number} is already booked for {date} at {time_slot}. Please pick another slot."
                )

        return cleaned_data
