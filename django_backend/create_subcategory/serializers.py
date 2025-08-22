# AUGUST 22
# SAMIP REGMI

# DUMMY CODE
from rest_framework import serializers
from sqldb_app.models import Category , SubCategory

class CreateSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['categoryID','subCategoryId','subCategoryName']

    # CHECK IF SUB CATEGORY HAS SAME NAME AND BELONGS TO SAME CATEGORY
    def validate(self, data):
        # TODO: FIX THS
        # SENDING SAME ERROR MESSAGE FOR THE SUB CATEGORY THAT DOESNT EVEN EXIST ,


        if SubCategory.objects.filter(subCategoryName__iexact = data['subCategoryName'],categoryID = data['categoryID']):
            raise serializers.ValidationError("SubCategory with this name already exists in this Category")
        return data

    def create(self, validated_data):
        subcategory = SubCategory.objects.create(**validated_data)
        return subcategory
