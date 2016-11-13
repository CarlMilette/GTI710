from . import models
from rest_framework import serializers

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SaleOrderLine
        fields = ('id', 'product_id')