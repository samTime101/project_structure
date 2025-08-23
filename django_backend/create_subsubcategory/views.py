# AUGUST 23
# SAMIP REGMI
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateSubSubCategorySerializer
from sqldb_app.models import SubSubCategory

class CreateSubSubCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # ONLY ADMIN AND STAFF CAN CREATE SUBSUBCATEGORY
        if not request.user.is_superuser and not request.user.is_staff:
            response_data = {
                "message": "You do not have permission to create a subcategory",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)

        serializer = CreateSubSubCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subsubcategory = serializer.save()

        response_data = {
            "message": "Sub SubCategory created successfully",
            "subsubcategory": {
                "id": subsubcategory.subSubCategoryId,
                "name": subsubcategory.subSubCategoryName,
                "subCategoryId": subsubcategory.subCategoryID.subCategoryId,
                "subCategoryName": subsubcategory.subCategoryID.subCategoryName,
                "categoryId": subsubcategory.subCategoryID.categoryID.categoryId,
                "categoryName": subsubcategory.subCategoryID.categoryID.categoryName,
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

    def get(self, request):
        subsubcategories = SubSubCategory.objects.all()
        serializer = CreateSubSubCategorySerializer(subsubcategories, many=True)
        response_data = {
            "message": "Sub SubCategory list retrieved",
            "subsubcategories": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)