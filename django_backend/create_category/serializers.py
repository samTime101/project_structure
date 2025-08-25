# AUGUST 22
# SAMIP REGMI

from rest_framework import serializers
from sqldb_app.models import Category

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryId','categoryName']

    # SAME CATEGORY NOT ALLOWED , HAVE TO ASK WITH SIR TO DIRECTLY INTEGRATE THIS IN CATEGORY MODEL
    # CHANGED TO VALIDATE FOR VALIDATING MULTIPLE FIELDS [FOR FUTURE]

    def validate(self, data):
        # THE CATEGORY NAME CANNOT BE EXISTING CATEGORY NAME 
        if Category.objects.filter(categoryName__iexact=data['categoryName']).exists():
            raise serializers.ValidationError("Category with this name already exists")
        return data

    def create(self,validated_data):
        category = Category.objects.create(**validated_data)
        return category

