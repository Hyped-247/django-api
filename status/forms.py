from django.core.exceptions import ValidationError
from django.forms import ModelForm
from status.models import Status


class StatusForm(ModelForm):
	class Meta:
		model = Status
		fields = ['user', 'content', 'image']
		
	def clean(self, *args, **kwargs):
		image = self.cleaned_data.get('image', None)
		content = self.cleaned_data.get('content', None)
		if content == "":
			content = None
		if image is None and content is None:
			raise ValidationError("You need to either have an image or content or both.")
		return self.cleaned_data
		








