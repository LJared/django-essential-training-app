from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from .models import Note
from .forms import NoteForm

# When using class-based views such as ListView or DetailView,
# we need to comply with the naming conventions of the templates.
# Otherwise, the name of the template is specified in the property 'template_name'
class NoteCreateView(CreateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NoteForm


class NoteUpdateView(UpdateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NoteForm


class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/smart/notes'
    template_name = 'notes/note_delete.html'


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
