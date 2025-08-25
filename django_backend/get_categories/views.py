# SAMIP REGMI
# AUGUST 23

# VERY BAD NESTED LOOP

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from sqldb_app.models import Category , SubCategory , SubSubCategory


class GetCategoriesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # WHEN USER SENDS A GET REQUEST TO THIS ENDPOINT
        # SEND ALL DETAILS OF CATEGORIES, SUBCATEGORIES, SUBSUBCATEGORIES

        # FETCH ALL CATEGORIES
        categories = Category.objects.all()
        data = []
        for category in categories:

            #SELECT FROM SUBCATEGORIES WHERE categoryID = category 
            subcategories = SubCategory.objects.filter(categoryID=category)
            subcategory_list = []
            for subcategory in subcategories:
                # SAME HERE ALSO AND BELOW
                subsubcategories = SubSubCategory.objects.filter(subCategoryID=subcategory)
                subsubcategory_list = []

                for subsubcategory in subsubcategories:
                    subsubcategory_list.append({
                        "id": subsubcategory.subSubCategoryId,
                        "name": subsubcategory.subSubCategoryName
                    })
                subcategory_list.append({
                    "id": subcategory.subCategoryId,
                    "name": subcategory.subCategoryName,
                    "subSubCategories": subsubcategory_list
                })
            data.append({
                "id": category.categoryId,
                "name": category.categoryName,
                "subCategories": subcategory_list
            })
        response_data={
            "categories": data,
        }
        return Response(response_data, status=status.HTTP_200_OK)


# TODO: - BREAK INTO TWO FUNCTIONS
# GET_SUBCATS AND GET_SUBSUBCATS
# GET SUBCATS : ARGUMENT: CATS
# LOOPS -> CALLS SUBSUBCATS
# GET SUBSUBCATS : ARGUMENT: SUBCATS

# FOR CAT IN CATS
# -> CALLS