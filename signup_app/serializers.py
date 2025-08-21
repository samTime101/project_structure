from rest_framework import serializers
from sqldb_app.models import User

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'phonenumber', 'firstname', 'lastname', 'is_active', 'is_staff', 'is_superuser', 'password']
        extra_kwargs = {'password': {'write_only': True}} # DONT RETURN PASSWORD IN RESPONSE

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
