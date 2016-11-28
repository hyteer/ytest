from django.db import models
from django.utils import timezone

# Create your models here.

class Record(models.Model):
	"""docstring for Custmer"""
	name = models.CharField(max_length=30)
	record_type = models.ForeignKey("RecordType", null=True, blank=True)
	content = models.CharField(max_length=40)
	description = models.TextField(null=True, blank=True)

class Order(models.Model):

	order_no = models.CharField(max_length=40)
	total_fee = models.DecimalField(max_digits=8, decimal_places=4)
	trade_type = models.ForeignKey('TradeType', null=True, blank=True)
	created_time = models.DateTimeField('Created Time', default=timezone.now())
	mch_id = models.CharField(max_length=20)
	related_project = models.ForeignKey('Project')
	remark = models.TextField()


class RecordType(models.Model):

	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class TradeType(models.Model):

	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Project(models.Model):

	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name



