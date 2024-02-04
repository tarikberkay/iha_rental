from rest_framework import serializers
from .models import Iha, Kiralama

class IhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iha
        fields = '__all__'

class KiralamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kiralama
        fields = '__all__'
