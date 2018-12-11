"""
	CSRFExemptMixin is going to allow us to send and get data back and forth without being authonticated.
"""
import json
from django.http import JsonResponse
from django.views.generic.base import View
from authors.api.mixins import CSRFExemptMixin
from authors.forms import AuthorForm
from authors.models import Author
from django.core.serializers import serialize


def get_object(pk):
	author_obj = Author.objects.filter(pk=pk)
	if author_obj.count() == 1:
		return author_obj.first()
	return None


class ListCreateModelAuthorAPI(CSRFExemptMixin, View):
	
	def get(self, *args, **kwargs):
		data = serialize("json", Author.objects.all())
		return JsonResponse(data, safe=False)
	
	def post(self, *args, **kwargs):
		data = {}
		form_author = AuthorForm(self.request.POST)
		if form_author.is_valid():
			author_obj = form_author.save(commit=True)
			data['message'] = 'success'
			data['object created'] = serialize('json', [author_obj])
		else:
			data['message'] = 'failure'
		return JsonResponse(data, safe=False)


class DetailUpdateDeleteModelAuthorAPI(CSRFExemptMixin, View):
	
	def get(self, *args, **kwargs):
		data = {}
		author_obj = get_object(self.kwargs.get('pk'))
		if author_obj:
			data['message'] = 'success'
			data['object created'] = serialize('json', [author_obj])
			return JsonResponse(data, safe=False, status=200)
		else:
			data['message'] = 'Object doesn\'t exists.'
			return JsonResponse(data, safe=False, status=404)
	
	def put(self, *args, **kwargs):
		data = {}
		author_obj = get_object(self.kwargs.get('pk'))
		passed_data = json.loads(self.request.body)
		if author_obj:
			form_author = AuthorForm(passed_data, instance=author_obj)
			if form_author.is_valid():
				form_author.save()
				data['message'] = 'success'
				data['object created'] = serialize('json', [author_obj])
				return JsonResponse(data, safe=False, status=200)
			else:
				data['message'] = form_author.errors
				return JsonResponse(data, safe=False, status=206)
		else:
			data['message'] = 'Object doesn\'t exists.'
			return JsonResponse(data, safe=False, status=404)
	
	def delete(self, *args, **kwargs):
		data = {}
		author_obj = Author.objects.filter(pk=self.kwargs.get('pk'))
		if author_obj.count() == 1:
			author_obj.first().delete()
			data['message'] = 'This object has been deleted.'
			return JsonResponse(data, safe=False, status=200)
		else:
			data['message'] = 'Object doesn\'t exists.'
			return JsonResponse(data, safe=False, status=404)


