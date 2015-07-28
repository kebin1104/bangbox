from django.contrib.auth.models import User, Group

from rest_framework import serializers

from bangbox.models import Bangbox_user, event

class bangboxEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = [
            'id', 'title', 'sub', 'address', 'price', 'datetime', 'imageURL',
        ]