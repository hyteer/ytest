# encoding: utf-8
from django.db import models

# Create your models here.

class Customer(models.Model):
	"""docstring for Custmer"""
	customer_name = models.CharField(max_length=30)
	phone_number = models.CharField(blank=True, max_length=20,null=True)
	email = models.EmailField(blank=True,null=True)
	start_date = models.DateField(blank=True, null=True)
	region = models.ForeignKey("Region", null=True, blank=True)
	address = models.TextField(blank=True, null=True)
	remark = models.TextField(blank=True, null=True)
	customer_type = models.ForeignKey("CustomerType", null=True, blank=True)

	def __str__(self):
		return self.customer_name

	def get_latest(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		#latest = self.followrecords_set.filter().order_by('-id')[:1]
		#latest = self.followrecords_set.filter().order_by('-id')[0]
		try:
			latest = self.followrecords_set.filter().order_by('-id')[0].record_text
			return latest
		except (IndexError):
			return 'No Record'


	'''
	def latest_follow_record(self):
		latet_record = self.followrecords_set
		self.fo
		return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now
		#return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
	'''
	'''
	def is_recently_followed(self):

		now = timezone.now()
		return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	'''

	
		

class CustomerType(models.Model):
	"""docstring for CustomerType"""
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class FollowRecords(models.Model):

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	record_text = models.CharField(verbose_name='记录', max_length=80)
	follow_type = models.ForeignKey("CommunicateType", null=True, blank=True)

	def get_latest_record(self):
		return self.values('record_text').order_by('-id')[0]

	


class CommunicateType(models.Model):

	name = models.CharField(max_length=10)
	def __str__(self):
		return self.name 

class Region(models.Model):

	name = models.CharField(verbose_name='地区', max_length=20)
	def __str__(self):
		return self.name 
