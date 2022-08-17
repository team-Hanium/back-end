from rest_framework import serializers
from .models import Sisul


class SisulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sisul
        fields = ['id', 'name', 'longitude', 'latitude', 'zipcode', 'category', 'info']
