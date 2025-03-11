from django import forms
from .models import WaterBooking

class WaterBookingForm(forms.ModelForm):
    class Meta:
        model = WaterBooking
        fields = ['name', 'address', 'phone_number', 'number_of_tins', 'payment_method']