from rest_framework import serializers
from .models import *

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'phonenumber', 'firstname', 'lastname', 'is_active', 'is_staff', 'is_superuser']
    def create(self, validated_data):
        return super().create_user(**validated_data) # DICT TO ARGS FOR CREATE_USER MODEL