from rest_framework import serializers
from .models import CustomUser

# Serializer to serialize the request and response
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'full_name', 'user_type', 'password','is_active')
        extra_kwargs = {'password': {'write_only': True}}

    # manipulating inbuild create
    def create(self, validated_data):
        # Getting user_type from the request
        user_type = validated_data.get('user_type', None)
        # Checking user_type is not None
        if user_type is not None:
            user = CustomUser(
                email=validated_data['email'],
                full_name=validated_data['full_name'],
                user_type=user_type
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        else:
            raise serializers.ValidationError("user_type cannot be None")