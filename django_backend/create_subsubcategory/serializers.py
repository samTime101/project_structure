# SAMIPREGMI
# AUGUST 23


from rest_framework import serializers
from sqldb_app.models import SubSubCategory

class CreateSubSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSubCategory
        fields = ['subCategoryID', 'subSubCategoryId', 'subSubCategoryName']

    # NO SAME SUBSUBCATEGORY NAME IN THE SAME SUBCATEGORY
    def validate(self, data):
        if SubSubCategory.objects.filter(
            subSubCategoryName__iexact=data['subSubCategoryName'],
            subCategoryID=data['subCategoryID']
        ).exists():
            raise serializers.ValidationError("SubSubCategory with this name already exists in this SubCategory")
        return data

    def create(self, validated_data):
        return SubSubCategory.objects.create(**validated_data)
