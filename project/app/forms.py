from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ['company', 'name', 'direction', 'date', 'experience_required', 'education_required']
