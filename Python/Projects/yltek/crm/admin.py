# encoding: utf-8
import sys;

reload(sys);
sys.setdefaultencoding("utf8")

from django.contrib import admin

from .models import Customer, CustomerType, FollowRecords, CommunicateType, Region

# Register your models here.

class FollowRecordsInline(admin.TabularInline):
    model = FollowRecords
    verbose_name = '跟踪记录'
    #raw_id_fields = ("customer",)
    
    fieldsets = [
    	('跟踪方式',{'fields': ['follow_type']}),
		('跟踪记录', {'fields': ['record_text']}),
	]
	
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['customer_name']}),
		('客户类型', {'fields': ['customer_type']}),
		('电话', {'fields': ['phone_number']}),
		('Email', {'fields': ['email']}),
		('地区', {'fields': ['region']}),
		('开始时间', {'fields': ['start_date']}),
		('备注', {'fields': ['remark'], 'classes': ['collapse']}),
		#('跟踪记录', {'fields': [FollowRecordsInline]}),
	]
	#inlines = ('客户类型', {'fields':[FollowRecordsInline]})
	inlines = [FollowRecordsInline]
	list_display = ('customer_name', 'customer_type', 'phone_number', 'email', 'get_latest','region')
	#fields = ['question_text','pub_date']
	list_filter = ['customer_type', 'start_date']
	search_fields = ['customer_name']
	#date_hierarchy = 'pub_date'

admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerType)
admin.site.register(CommunicateType)
admin.site.register(Region)
