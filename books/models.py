from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=500)
	genre = models.CharField(max_length=255, blank=True, null=True)
