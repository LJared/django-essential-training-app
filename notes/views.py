from django.shortcuts import render
from django.http import Http404
from .models import Note

def list(request):
    """
    Get all notes and render them.
    """
    # Get all notes from the database.
    all_notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, note_id):
    """
    Get a single note and render it.
    If the note doesn't exist, raise a 404 error.

    Args:
        request (HttpRequest): The request object.
        note_id (int): The ID of the note to retrieve.
            This parameter has to have the same name as the URL pattern.

    Raises:
        Http404: If the note doesn't exist.
    """
    # Get a single note from the database.
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
