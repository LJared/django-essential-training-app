"""Views for the notes app."""
from django.forms import BaseModelForm
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note
from .forms import NoteForm

NOTE_LIST_URL = '/smart/notes'

# When using class-based views such as ListView or DetailView,
# we need to comply with the naming conventions of the templates.
# Otherwise, the name of the template is specified in the property 'template_name'
class NoteCreateView(CreateView):
    model = Note
    success_url = NOTE_LIST_URL
    form_class = NoteForm

    def form_valid(self, form: BaseModelForm) -> HttpResponseRedirect:
        """
        Override the default form_valid method to add the current user as the
        author of the note.
        """
        # pylint: disable=attribute-defined-outside-init
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteUpdateView(UpdateView):
    model = Note
    success_url = NOTE_LIST_URL
    form_class = NoteForm


class NoteDeleteView(DeleteView):
    model = Note
    success_url = NOTE_LIST_URL

    # In case the template name is not specified in the property 'template_name'
    # Django will try to find a template with the name 'note_confirm_delete.html'
    template_name = 'notes/note_delete.html'


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    login_url = '/login'

    def get_queryset(self):
        """
        Override the default queryset to only return
        notes created by the current user.
        """
        return self.request.user.note_ids.all()


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
