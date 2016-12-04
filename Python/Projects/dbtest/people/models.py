from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10, default=None, blank=True)
    email = models.EmailField(default=None, blank=True)
    created_time = models.DateTimeField(default=timezone.now)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

    def __str__(self):
    	return self.name

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)
    
class MyUser(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to='photo', null=True, blank=True)