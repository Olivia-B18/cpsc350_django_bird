from django import forms

from .models import Bird, Sighting

class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ['text', 'main_color', 'description']
        labels = {'text': 'Name',
                  'main_color': 'Main Color',
                  'description': 'Description',
                  }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_text(self):
        text = self.cleaned_data.get('text')
        # Check for duplicate bird name for this user
        existing = Bird.objects.filter(owner=self.user, text=text)
        # If editing, exclude the current bird from the check
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)
        if existing.exists():
            raise forms.ValidationError('You already have a bird with this name.')
        return text

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ['text', 'sighting_date']
        labels = {'text': '', 'sighting_date': 'Date'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
            'sighting_date': forms.DateInput(attrs={'type': 'date'}),
        }
