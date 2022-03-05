from rest_framework import serializers
from . models import categ,ProductFree

class categSerializer(serializers.ModelSerializer):
    class Meta:
        model = categ
        fields = '__all__'
class ProductFreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFree
        fields = '__all__'