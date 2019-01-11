from django.conf import settings
from django.db import models


def upload_image(instance, filename):
	return "updates/{0}/{1}".format(instance.user, filename)


class Update(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	context = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to=upload_image, blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.context
