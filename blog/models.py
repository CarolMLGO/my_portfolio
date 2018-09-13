from django.db import models

class Blog(models.Model):
    summary = models.CharField(max_length=500)
