# SAMIP REGMI
# AUGUST 23

# MODIFIED AUGUST 25

# TODO: https://stackoverflow.com/questions/27896603/how-to-validate-the-length-of-nested-items-in-a-serializer
# RESRTICT TO ONLY 4 OPTIONS 


from rest_framework import serializers
from mongodb_app.mongo import Option, Question
from sqldb_app.models import Category, SubCategory, SubSubCategory  # SQL models

# ADDING REQUIREED TRUE SO THAT IT DOES NOT ACCEPT NULL

class OptionSerializer(serializers.Serializer):
    optionId = serializers.CharField(required=True)
    text = serializers.CharField(required=True)

class CreateQuestionSerializer(serializers.Serializer):

    questionText = serializers.CharField(required=True)
    questionType = serializers.ChoiceField(choices=["single", "multiple"], required=True)
    options = OptionSerializer(many=True, required=True)
    correctAnswers = serializers.ListField(child=serializers.CharField(), required=True)
    # DEFAULT EASY
    difficulty = serializers.ChoiceField(choices=["easy", "medium", "hard"], default="easy")

    categoryId = serializers.IntegerField(required=True)
    # THE ELEMENT INSIDE LIST SHALL BE INTEGER
    subCategoryId = serializers.ListField(child=serializers.IntegerField(), required=True)
    # SAME HERE INT
    subSubCategoryId = serializers.ListField(child=serializers.IntegerField(), required=True)

    def create(self, validated_data):
        category_id = validated_data.get("categoryId")
        sub_category_ids = validated_data.get("subCategoryId", [])
        sub_sub_category_ids = validated_data.get("subSubCategoryId", [])

        # GET NAMES FROM SQL

        # SELECT CATEGORY NAME FROM CATEGORY WHERE categoryId = category_id
        if category_id:
            category_name = Category.objects.get(categoryId=category_id).categoryName

        # SELECT SUBCATEGORY NAMES FROM SUBCATEGORY WHERE subCategoryId IN (<sub_category_ids>) 
        # IN LIST FORM
        subcategory_names = list(
            SubCategory.objects.filter(subCategoryId__in=sub_category_ids)
            .values_list('subCategoryName', flat=True)
        )
        
        # SELECT SUBSUBCATEGORY NAMES FROM SUBSUBCATEGORY WHERE subSubCategoryId IN (<sub_sub_category_ids>)
        subsubcategory_names = list(
            SubSubCategory.objects.filter(subSubCategoryId__in=sub_sub_category_ids)
            .values_list('subSubCategoryName', flat=True)
        )

        question = Question(
            questionText=validated_data["questionText"],
            questionType=validated_data["questionType"],
            options=validated_data["options"],
            correctAnswers=validated_data["correctAnswers"],
            difficulty=validated_data["difficulty"],
            category=category_name,
            subCategory=subcategory_names,
            subSubCategory=subsubcategory_names
        )
        # SAVE TO MONGO
        question.save()
        return question
