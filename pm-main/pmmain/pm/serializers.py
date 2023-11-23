from rest_framework import serializers
from .models import PmStaff

class PmSerializer(serializers.ModelSerializer):
    class Meta:
        model = PmStaff
        fields = '__all__'