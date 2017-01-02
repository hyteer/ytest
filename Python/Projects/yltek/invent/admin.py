# encoding: utf-8
import sys;

reload(sys);
sys.setdefaultencoding("utf8")

from django.contrib import admin

from .models import Contact, Owner, Position, ProductCatgory, ProductStatus, Product, \
Customer, CustomerType, Region, SkuNo, Uucode, Barcode, Warehouse, ProductBatch

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['product_name']}),
		('catgory', {'fields': ['catgory']}),
		('warehouse', {'fields': ['warehouse']}),
		('sku', {'fields': ['sku']}),
		('owner', {'fields': ['owner']}),
		('status', {'fields': ['status']}),
		('批次', {'fields': ['batch']}),
		('uucode', {'fields': ['uucode']}),
		('创建时间', {'fields': ['created_time']}),
		('备注', {'fields': ['remark'], 'classes': ['collapse']}),
		#('跟踪记录', {'fields': [FollowRecordsInline]}),
	]

	list_display = ('product_name', 'catgory', 'sku', 'owner', 'uucode','batch')
	#fields = ['question_text','pub_date']
	list_filter = ['status', 'warehouse', 'catgory', 'owner', 'batch']
	search_fields = ['product_name']
	#date_hierarchy = 'pub_date'


class CustomerAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['customer_name']}),
		('客户类型', {'fields': ['customer_type']}),
		('电话', {'fields': ['phone_number']}),
		('联系人', {'fields': ['contact']}),
		('地区', {'fields': ['region']}),
		('开始时间', {'fields': ['start_date']}),
		('备注', {'fields': ['remark'], 'classes': ['collapse']}),
		#('跟踪记录', {'fields': [FollowRecordsInline]}),
	]

	list_display = ('customer_name', 'customer_type', 'phone_number','region')
	#fields = ['question_text','pub_date']
	list_filter = ['customer_type', 'start_date', 'region']
	search_fields = ['customer_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Owner)
admin.site.register(Position)
admin.site.register(ProductCatgory)
admin.site.register(ProductStatus)
admin.site.register(CustomerType)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Region)
admin.site.register(SkuNo)
admin.site.register(Uucode)
admin.site.register(Barcode)
admin.site.register(Warehouse)
admin.site.register(ProductBatch)


