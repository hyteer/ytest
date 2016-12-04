# encoding: utf-8
from django.contrib import admin

from .models import Group, Room, Message
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
	'''
	fieldsets = [
		#(None, {'fields': ['label','get_groups']}),
		('name', {'fields': ['name']}),
		('time',{'fields': ['time']}),
	]
	'''
	#inlines = ('客户类型', {'fields':[FollowRecordsInline]})
	#inlines = [MessageInline]
	list_display = ('label', 'name', 'time', 'get_groups')
	#fields = ['question_text','pub_date']
	list_filter = ['groups', 'label']
	search_fields = ['label']
	#date_hierarchy = 'pub_date'

class MessageAdmin(admin.ModelAdmin):
	list_display = ('room', 'message', 'sender', 'time')
	list_filter = ['room', 'time']

admin.site.register(Group)
admin.site.register(Room, RoomAdmin)

admin.site.register(Message, MessageAdmin)
