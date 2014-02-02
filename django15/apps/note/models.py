from django.db import models

class Note(models.Model):
    """
    Note model with title, body, time of creation fields
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
