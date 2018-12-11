from django.contrib import admin
from status.forms import StatusForm
from status.models import Status


class StatusAdmin(admin.ModelAdmin):
	list_display = ['user', 'content', 'image']
	form = StatusForm
	

admin.site.register(Status, StatusAdmin)
