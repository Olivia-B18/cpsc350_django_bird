from django import forms

from .models import Bird, Sighting

class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ['text', 'main_color', 'description']
        labels = {'text': '',
                  'main_color': 'Main Color',
                  'description': 'Description',
                  }

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ['text', 'sighting_date']
        labels = {'text': '', 'sighting_date': 'Date'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
            'sighting_date': forms.DateInput(attrs={'type': 'date'}),
        }
