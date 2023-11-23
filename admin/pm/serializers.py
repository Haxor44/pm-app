from rest_framework import serializers
from .models import Pmforms
class PmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pmforms
        fields = '__all__'