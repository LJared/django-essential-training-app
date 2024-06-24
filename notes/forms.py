from typing import Any
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter a title here',
                'class': 'form-control my-5'
            }),
            'text': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-control mb-5'
            }),
        }
        labels = {
            'text': 'Write your note here',
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
