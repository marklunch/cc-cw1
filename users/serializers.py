from rest_framework import serializers
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password') 
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'blank': True},
            'last_name': {'blank': True},
            'email': {'blank': True},
            'is_staff':{'blank:': True}
            }