from django.forms import ModelForm
from authors.models import Author


class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = ['name']
