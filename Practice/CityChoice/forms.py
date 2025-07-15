from django import forms
from .models import Profile, City

class ProfileForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Select City")

    class Meta:
        model = Profile
        fields = ['name', 'city']

