from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Group(models.Model):
    """docstring for Group"""
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)

    def __str__(self):
    	return self.name


class Room(models.Model):
    name = models.CharField(max_length=100, blank=True)
    label = models.SlugField(unique=True)
    time = models.DateTimeField(default=timezone.now, db_index=True)
    groups = models.ManyToManyField(Group, blank=True)
    #group = models.ForeignKey(Group, null=True, blank=True)
    #message = models.ForeignKey(Message, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.label

    def get_groups(self):
    	return [group.name for group in self.groups.all()]

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', null=True, blank=True)
    sender = models.CharField(max_length=30, default='anonymous')
    message = models.TextField(blank=True)
    time = models.DateTimeField(default=timezone.now, db_index=True)
    #rooms = models.ManyToManyField(Room, blank=True)

    def __str__(self):
        return "sender:%s,msg:%s" % (self.sender,self.message)

    def get_rooms(self):
    	return self.room
    	#return [room.label for room in self.rooms.all()]