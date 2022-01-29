from pyexpat import model
from django.db import models

# Create your models here.

class AddEvent(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField()
    detail = models.TextField()

    def __str__(self):
        return self.title