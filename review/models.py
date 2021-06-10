from django.db import models

class Review(models.Model):
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=20)
    date = models.DateField(blank=False, null=False, auto_now_add=True)
