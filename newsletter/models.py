from django.db import models
#from django.utils.timezone import *

# Create your models here.


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):  # python 3.3 - __str__
        return self.email


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

