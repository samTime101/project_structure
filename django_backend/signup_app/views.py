from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSignupSerializer
from sqldb_app.models import User

class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # DIRECTLY SEND SERIALIZER DATA 
        # return Response(serializer.data, status=status.HTTP_201_CREATED)

        #RETURNING CUSTOM RESPONSE
        response_data = {
            "message": "User created successfully",
            "user":{
                "email": user.email,
                "username": user.username,
                "phonenumber": user.phonenumber,
                "firstname": user.firstname,
                "lastname": user.lastname,
            }
        } 
        return Response(response_data, status=status.HTTP_201_CREATED)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSignupSerializer(users, many=True)
        response_data = {
            "message": "User list retrieved successfully",
            "users": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
