from django import forms

from .models import Bird, Entry

class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ['text', 'main_color']
        labels = {'text': '', 'main_color': 'Main Color'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
