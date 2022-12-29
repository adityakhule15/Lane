from .models import count
from rest_framework import serializers


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = count
        fields = '__all__'