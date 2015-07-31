from django.contrib.auth.models import User, Group

from rest_framework import serializers

from bangbox.models import user, event, category, event_date, event_time

class bangboxEventSerializer(serializers.ModelSerializer):
    # user_id = models.ForeignKey(user)
    # title = models.CharField(null=False, max_length=26)
    # sub = models.CharField(null=False, max_length=50)
    # article = models.TextField()
    # address = models.CharField(null=False, max_length=50)
    # imageURL = models.URLField(null=False)
    class Meta:
        model = event
        fields = [
            'id', 'user_id', 'title', 'sub', 'article', 'address', 'imageURL',
        ]
        
class bangbox