from django.db import models
from django.conf import settings


class StatusQuerySet(models.QuerySet):
	pass


class StatusManger(models.Manager):

	def get_queryset(self):
		return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = StatusManger()

	def __str__(self):
		return str(self.content)[:50]













