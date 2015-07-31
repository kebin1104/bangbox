from django.db import models

# Create your models here.

class user(models.Model):
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.email

class event(models.Model):
    user_id = models.ForeignKey(user)
    category_id = models.ForeignKey('category')
    title = models.CharField(null=False, max_length=26)
    sub = models.CharField(null=False, max_length=50)
    article = models.TextField()
    address = models.CharField(null=False, max_length=50)
    imageURL = models.URLField(null=False)

    def __unicode__(self):
        return self.title

class category(models.Model):
    name = models.CharField(null=False, max_length=20)

    def __unicode__(self):
        return self.name

class event_date(models.Model):
    event_id = models.ForeignKey(event)
    date = models.DateField('date published')

    def __unicode__(self):
        return self.date

class event_time(models.Model):
    event_date_id = models.ForeignKey(event_date)
    time = models.TimeField()
    price = models.IntegerField(null=False)

    def __unicode__(self):
        return self.time