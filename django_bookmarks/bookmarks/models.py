from django.db import models

# Create your models here.

class user(models.Model):
    email = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)

    def _unicode_(self):
        return self.email
