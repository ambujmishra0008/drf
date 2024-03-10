from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=400, null=True, blank=True)
