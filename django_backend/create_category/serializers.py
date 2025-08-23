# AUGUST 22
# SAMIP REGMI

from rest_framework import serializers
from sqldb_app.models import Category

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryId','categoryName']

    # SAME CATEGORY NOT ALLOWED , HAVE TO ASK WITH SIR TO DIRECTLY INTEGRATE THIS IN CATEGORY MODEL
    def validate_categoryName(self, value):
        if Category.objects.filter(categoryName__iexact=value).exists():
            raise serializers.ValidationError("Category with this name already exists")
        return value

    def create(self,validated_data):
        category = Category.objects.create(**validated_data)
        return category

