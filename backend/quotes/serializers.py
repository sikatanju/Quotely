from rest_framework import serializers
from .models import Quote, Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta: 
        model = Category
        # fields = ['id', 'name']
        fields = '__all__'


class QuoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'category']