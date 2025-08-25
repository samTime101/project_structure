# SAMIP REGMI
# AUGUST 23


from rest_framework import serializers
from mongodb_app.mongo import Option, Question
from sqldb_app.models import Category, SubCategory, SubSubCategory  # SQL models


class SelectQuestionSerializer(serializers.Serializer):
    # IF ALL EMPTY JUST RETURN ALL QUESTIONS
    categoryIds = serializers.ListField(child=serializers.IntegerField(), required=False, allow_empty=True)
    subCategoryIds = serializers.ListField(child=serializers.IntegerField(), required=False, allow_empty=True)
    subSubCategoryIds = serializers.ListField(child=serializers.IntegerField(), required=False, allow_empty=True)


    def get_questions(self):
        # GET IDS 
        category_ids = self.validated_data.get("categoryIds", [])
        sub_category_ids = self.validated_data.get("subCategoryIds", [])
        sub_sub_category_ids = self.validated_data.get("subSubCategoryIds", [])

        # FETCH NAMES FROM SQL DB
        # SELECT categoryName FROM Category WHERE categoryId IN (category_ids)
        categories = list(Category.objects.filter(categoryId__in=category_ids).values_list("categoryName", flat=True))
        # SAME
        subCategories = list(SubCategory.objects.filter(subCategoryId__in=sub_category_ids).values_list("subCategoryName", flat=True))
        # SAME
        subSubCategories = list(SubSubCategory.objects.filter(subSubCategoryId__in=sub_sub_category_ids).values_list("subSubCategoryName", flat=True))

        query_parts = []
        if categories:
            query_parts.append({"category": {"$in": categories}})
        if subCategories:
            query_parts.append({"subCategory": {"$in": subCategories}})
        if subSubCategories:
            query_parts.append({"subSubCategory": {"$in": subSubCategories}})


        # print(query_parts)
        if query_parts:
            # https://onecompiler.com/mongodb/43ujbj8k6
            return Question.objects(__raw__={"$or": query_parts})
        
        # IF ALL EMPTY JUST RETURN ALL QUESTIONS
        # TODO: MAY BE I NEED TO FIX THIS LATER
        else:
            return Question.objects.all()
