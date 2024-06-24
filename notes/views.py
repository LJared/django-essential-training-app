from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView
from .models import Note


# When using class-based views such as ListView or DetailView,
# we need to comply with the naming conventions of the templates.
# Otherwise, the name of the template is specified in the property 'template_name'
class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'text']
    success_url = '/smart/notes'


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
