from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from status.api.serializers import StatusSerializer
from status.models import Status


class ListCreateModelStatusAPI(CreateModelMixin, ListAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	authentication_classes = [SessionAuthentication]
	# queryset = Status.objects.all()
	serializer_class = StatusSerializer
	
	# get_queryset method will filter the query set that is returned by ListModelStatusAPI or return all the objects.
	def get_queryset(self):
		qs = Status.objects.all()
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(content__icontains=query)
		return qs
	
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
	

class DetailUpdateDeleteModelStatusAPI(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	authentication_classes = [SessionAuthentication]
	queryset = Status.objects.all()
	serializer_class = StatusSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
	
	# lookup_field = 'id'

	# def get_object(self, *args, **kwargs):
	# 	kwargs = self.kwargs
	# 	kw_id = kwargs.get('abc')
	# 	status_obj = get_object_or_404(Status, pk=kw_id)
	# 	return status_obj


