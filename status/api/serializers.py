from rest_framework import serializers
from status.models import Status

"""
A note about serializers. They can turn our objects to JSON. And it can also turn validate data.
"""


class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ['user', 'content', 'image']
		read_only_fields = ['user']
