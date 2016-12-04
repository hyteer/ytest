# encoding: utf-8
from django.contrib import admin
'''
from .models import Room, Message
# Register your models here.

class MessageInline(admin.TabularInline):
    model = Message
    verbose_name = 'Message Records'
    #raw_id_fields = ("customer",)
    
    fieldsets = [
    	('message',{'fields': ['message']}),
		('timestamp', {'fields': ['timestamp']}),
	]
	
    extra = 1


class RoomAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['label']}),
		('name', {'fields': ['name']}),
		('Created Time', {'fields': ['time']}),
	]
	#inlines = ('客户类型', {'fields':[FollowRecordsInline]})
	#inlines = [MessageInline]
	list_display = ('label', 'name', 'time')
	#fields = ['question_text','pub_date']
	list_filter = ['label', 'time']
	search_fields = ['label']
	#date_hierarchy = 'pub_date'

class MessageAdmin(admin.ModelAdmin):
	list_display = ('message', 'sender', 'time')
	list_filter = ['rooms','time']


admin.site.register(Room, RoomAdmin)

admin.site.register(Message, MessageAdmin)
'''