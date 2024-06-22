from django.contrib import admin
from . import models

class NoteAdmin(admin.ModelAdmin):
    # This is a list of fields that will be displayed
    # in the admin site as table columns of the Note model.
    list_display = ('title', 'text', 'created_at',)

admin.site.register(models.Note, NoteAdmin)
