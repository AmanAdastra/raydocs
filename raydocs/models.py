from django.db import models

# Create your models here.
class MyIdea(models.Model):
    name = models.CharField(max_length=100)
    idea = models.TextField()