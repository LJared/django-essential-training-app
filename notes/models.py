from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='note_ids')
    created_at = models.DateTimeField(auto_now_add=True)

    def concat_title_and_text(self):        
        if self.title and self.text:
            return self.title + " => " + self.text
        return "Not a valid note"
