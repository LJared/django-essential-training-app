from django.shortcuts import render
from .models import Note

def list(request):
    """
    Get all notes and render them.
    """
    # Get all notes from the database.
    all_notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})
