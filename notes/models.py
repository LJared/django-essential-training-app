from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def concat_title_and_text(self):        
        if self.title and self.text:
            return self.title + " => " + self.text
        return "Not a valid note"
