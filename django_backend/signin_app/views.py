from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSignInSerializer
from django.contrib.auth import login

class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        response_data = {
            "message": "User signed in successfully",
            "user": {
                "userId": user.userId,
                "email": user.email,
                "username": user.username,
                "phonenumber": user.phonenumber,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "is_active": user.is_active,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
