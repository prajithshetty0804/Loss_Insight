from rest_framework import serializers
from .models import PlantLoss

class PlantLossSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantLoss
        fields = '__all__'
