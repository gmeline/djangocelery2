from django import forms
from .models import IP

class IpAdressForm (forms.ModelForm):
    class Meta:
        model = IP
        fields=['number']