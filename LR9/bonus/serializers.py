from rest_framework import serializers

from .models import UserLevel

class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevel
        fields = ('spend', 'level')
