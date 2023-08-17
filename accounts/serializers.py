from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class NormalUserRegistrationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password_2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'password_1', 'password_2', 
            'user_type', 'country_code', 'mobile', 'education', 'gender', 
            'company_website', 'designation', 'annual_revenue', 'instagram_profile', 
            'linkedin_profile', 'portfolio', 'is_active'
        )

    def validate(self, data):
        if data['password_1'] != data['password_2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_2')
        password = validated_data.pop('password_1')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class OtherUserRegistrationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password_2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'password_1', 'password_2', 'user_type')

    def validate(self, data):
        if data['password_1'] != data['password_2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_2')
        password = validated_data.pop('password_1')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
