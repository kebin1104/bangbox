from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bangbox_user(models.Model, User):
    email = models.EmailField()
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.email

    def save(self, *args, **kwargs):

        self.set_password(self.password)

        super(Bangbox_user, self).save(*args, **kwargs)