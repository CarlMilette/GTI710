from . import models
from rest_framework import serializers

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ('id', 'product_id', 'rating')