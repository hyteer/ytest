# encoding: utf-8
from __future__ import unicode_literals
import datetime;  
import random; 


from django.db import models

# Functions
def gen_unique_num():
	nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S");#生成当前时间  
	randomNum=random.randint(0,100);#生成的随机整数n，其中0<=n<=100  
	if randomNum<=10:  
	    randomNum=str(0)+str(randomNum);  
	uniqueNum=str(nowTime)+str(randomNum);  
	return uniqueNum


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    remark = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name


class Customer(models.Model):
	"""docstring for Custmer"""
	customer_name = models.CharField(max_length=30)
	customer_type = models.ForeignKey("CustomerType", null=True, blank=True)
	phone_number = models.CharField(blank=True, max_length=20,null=True)
	contact = models.ManyToManyField(Contact,blank=True,)
	start_date = models.DateField(blank=True, null=True)
	region = models.ForeignKey("Region", null=True, blank=True)
	address = models.TextField(blank=True, null=True)
	remark = models.TextField(blank=True, null=True)
	

	def __str__(self):
		return self.customer_name


class CustomerType(models.Model):
	"""docstring for CustomerType"""
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name


class Region(models.Model):

	name = models.CharField(verbose_name='地区', max_length=20)
	def __str__(self):
		return self.name 


class Owner(models.Model):
	"""docstring for Supplier"""
	name = models.CharField(max_length=20)
	phone = models.CharField(blank=True, max_length=20)
	contact = models.ManyToManyField(Contact)
	remark = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name


class Position(models.Model):

	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name



class ProductCatgory(models.Model):
	"""docstring for ProductCatgory"""
	name = models.CharField(max_length=20)
	desc = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name

class ProductBatch(models.Model):
	"""docstring for ProductCatgory"""
	name = models.CharField(max_length=30)
	created_time = models.DateField(blank=True, null=True)
	desc = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name


class ProductStatus(models.Model):
	"""docstring for ProductStatus"""
	name = models.CharField(max_length=20)
	desc = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return self.name

class Uucode(models.Model):
	code = models.CharField(max_length=30)
	
	def __str__(self):
		return self.code

class SkuNo(models.Model):
	sku = models.CharField(max_length=30)
	
	def __str__(self):
		return self.sku

class Barcode(models.Model):
	code = models.CharField(max_length=30)
	
	def __str__(self):
		return self.code



class Warehouse(models.Model):
	"""docstring for ProductStatus"""
	name = models.CharField(max_length=20)
	position = models.ManyToManyField(Position)
	desc = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return self.name


class Product(models.Model):
	"""docstring for Custmer"""
	product_name = models.CharField(max_length=30)
	created_time = models.DateField(blank=True, null=True)
	catgory = models.ForeignKey("ProductCatgory", null=True, blank=True)
	#price = models.EmailField(blank=True,null=True)
	status = models.ForeignKey("ProductStatus", null=True, blank=True)
	owner = models.ForeignKey("Owner", null=True, blank=True)
	sku = models.ForeignKey("SkuNo", max_length=30)
	uucode = models.ForeignKey("Uucode", max_length=30, default=gen_unique_num())
	barcode = models.CharField(null=True, max_length=30)
	warehouse = models.ManyToManyField(Warehouse, blank=True)
	batch = models.ForeignKey("ProductBatch",blank=True, null=True)
	remark = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.product_name


''' 产品仓库和客户的连接表
class Inventory(models.Model):
	"""docstring for ProductStatus"""
	name = models.CharField(max_length=20)
	position = models.ManyToManyField(Position)
	product = models.ManyToManyField(Product)
	status = models.ForeignKey("ProductStatus", null=True, blank=True)
	desc = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return self.name
'''




class Operator(models.Model):

	username = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	phone = models.CharField(blank=True, max_length=20)
	remark = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name











