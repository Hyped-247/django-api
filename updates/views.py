from django.core.serializers import serialize
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django_api.mixins import JsonResponseMixin
from updates.models import Update


def update_model_detail_view(request):
	data = {
		"count": 100,
		"data": "some new information"
	}
	return JsonResponse(data)


class JsonCBV(View):
	
	def get(self, request, *args, **kwargs):
		data = {
			"count": 100,
			"data": "some new information"
		}
		return JsonResponse(data)
	

class JsonCBV2(JsonResponseMixin, View):
	
	def get(self, request, *args, **kwargs):
		data = {
			"count": 100,
			"data": "some new information"
		}
		return self.render_to_json_response(data)


class SerializedView(View):
	
	def get(self, request, *args, **kwargs):
		update_obj = Update.objects.all()
		data = serialize('json', update_obj)  # this is how your turn a Django object to JSON.
		return HttpResponse(data, content_type='application/json')


class SerializedDetail(View):
	
	def get(self, request, *args, **kwargs):
		update_obj = Update.objects.get(pk=1)
		data = serialize('json', [update_obj, ])  # this is how your turn a Django object to JSON.
		return HttpResponse(data, content_type='application/json')
