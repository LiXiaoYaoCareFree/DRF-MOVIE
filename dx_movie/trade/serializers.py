from rest_framework import serializers
from .models import Card, Order

class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = '__all__'


class OrderSerializer(serializers.ModelField):

    class Meta:
        model = Order
        fields = '__all__'