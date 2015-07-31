from django.contrib.auth.models import User, Group

from rest_framework import serializers

from bangbox.models import user, event, category, event_date, event_time

class bangboxUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = [
            'id', 'email', 'name',
        ]

class bangboxEventSerializer(serializers.ModelSerializer):
    # user_id = models.ForeignKey(user)
    # title = models.CharField(null=False, max_length=26)
    # sub = models.CharField(null=False, max_length=50)
    # category_id = models.ForeignKey('category')
    # article = models.TextField()
    # address = models.CharField(null=False, max_length=50)
    # imageURL = models.URLField(null=False)
    class Meta:
        model = event
        fields = [
            'id', 'user_id', 'title', 'sub', 'article', 'address', 'imageURL',
        ]
        
class bangboxCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = [
            'id', 'name',
        ]

class bangboxEventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = event_date
        fieldsa = [
            'id', 'event_id', 'date',
        ]

class bangboxEventTimeSerializer(serializers.ModelSerializer):

    # event_date_id = models.ForeignKey(event_date)
    # time = models.TimeField()
    # price = models.IntegerField(null=False)

    class Meta:
        model = event_time
        fieldsa = [
            'id', 'event_id', 'date',
        ]