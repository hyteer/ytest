from django.db import models
from django.utils import timezone

# Create your models here.

'''
class Group(models.Model):
    """docstring for Group"""
    name = models.CharField(max_length=100)
    desc = models.TextField()


class Room(models.Model):
    name = models.CharField(max_length=100)
    label = models.SlugField(unique=True)
    time = models.DateTimeField(default=timezone.now, db_index=True)
    group = models.ForeignKey(Group, null=True, blank=True)
    #message = models.ForeignKey(Message, on_delete=models.CASCADE)
    desc = models.TextField()

    def __str__(self):
        return self.label

class Message(models.Model):
    #room = models.ForeignKey(Room, related_name='messages', default=None)
    sender = models.CharField(max_length=30, default='anonymous')
    message = models.TextField()
    time = models.DateTimeField(default=timezone.now, db_index=True)
    rooms = models.ManyToManyField(Room)

    def __str__(self):
        return "sender:%s,msg:%s" % (self.sender,self.message)

'''

"""

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
"""