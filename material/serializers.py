from rest_framework import serializers

from material.models import Material


class MaterialListSerializer(serializers.ModelSerializer):
    total_quantity = serializers.IntegerField()

    class Meta:
        model = Material
        fields = ['id', 'name', 'quantity', 'price', 'total_quantity']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'quantity', 'price']
