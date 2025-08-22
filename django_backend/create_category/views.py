from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateCategorySerializer
from sqldb_app.models import Category

class CreateCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CreateCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save()
        response_data = {
            "message": "Category created successfully",
            "category":{
                "id": category.categoryId,
                "name": category.categoryName,
            }
        } 
        return Response(response_data, status=status.HTTP_201_CREATED)

    # FOR TESTING
    def get(self, request):
        categories = Category.objects.all()
        serializer = CreateCategorySerializer(categories, many=True)
        response_data = {
            "message": "Category list retrieved",
            "categories": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
