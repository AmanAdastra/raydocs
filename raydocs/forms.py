from django import forms
from .models import MyIdea
class IdeaForm(forms.ModelForm):
    class Meta:
        model = MyIdea
        fields = ['name','idea']