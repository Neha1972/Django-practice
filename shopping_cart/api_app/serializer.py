from rest_framework import serializers
from .models import CarItem


class CarItemsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=50)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CarItem
        fields = '__all__'
