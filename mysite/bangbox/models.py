from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bangbox_user(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.email
