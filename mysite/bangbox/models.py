from django.db import models

# Create your models here.

class Bangbox_user(models.Model):
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.email