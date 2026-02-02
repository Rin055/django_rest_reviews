from rest_framework import serializers

from .models import Review, Product


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'uuid', 'product', 'user', 'content', 'rating', 'created_at', 'updated_at']
        read_only_fields = ['id', 'uuid', 'created_at', 'updated_at']

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError('Rating must be between 1 and 5.')
        return value

    def validate_product(self, value):
       
        if value is None:
            return None
        if not Product.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError('Product does not exist.')
        return value

    def validate_content(self, value):
        if not value or len(value.strip()) < 5:
            raise serializers.ValidationError('Content is too short.')
        return value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'in_stock']

