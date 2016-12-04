from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True)
    label = models.SlugField(unique=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return self.label

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    sender = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return self.label


class Room2(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True)
    label = models.SlugField(unique=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return self.label


    