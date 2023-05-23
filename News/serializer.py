from rest_framework import serializers
from .models import News


class Newsserializer(serializers.ModelSerializer):
    class Meta:
        model