from rest_framework import serializers
from .models import ProductModel


def validate_price(value):
    if value < 0:
        raise serializers.ValidationError("Price cannot be negative")
    return value


def validate_name(value):
    if len(value) < 3:
        raise serializers.ValidationError("Name must be at least 3 characters long")
    return value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'price', 'creator']
        extra_kwargs = {
            'name': {'required': True},
            'price': {'required': True},
            'creator': {'required': True}
        }

    