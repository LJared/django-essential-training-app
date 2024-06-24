from typing import Any
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            
        }

    def clean_title(self):
        """
        Validates the title input by checking if it is too short,
        raising a ValidationError if it is.
        Returns the title after validation.
        """
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title is too short")
        return title
