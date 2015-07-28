from django.db import models

# Create your models here.

class Bangbox_user(models.Model):
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.email

class event(models.Model):
    title = models.CharField(null=False, max_length=20)
    sub = models.CharField(null=False, max_length=30)
    address = models.CharField(null=False, max_length=30)
    price = models.IntegerField(null=False)
    datetime = models.DateTimeField('date published')
    imageURL = models.URLField(null=False)

    def __unicode__(self):
        return self.title