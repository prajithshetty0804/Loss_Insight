from rest_framework import serializers
from .models import WeeklyLossRecord

class WeeklyLossSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyLossRecord
        fields = '__all__'
