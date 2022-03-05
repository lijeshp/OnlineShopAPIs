from app.serializer import ProductFreeSerializer
from . models import Cartlist,ItemsFree
from rest_framework import serializers

class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartlist
        fields = '__all__'

class ItemsfreeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ItemsFree()
        fields = '__all__'
        