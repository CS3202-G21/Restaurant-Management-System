from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Customer Serializer
class RegisterCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        customer.first_name = validated_data['first_name']
        customer.last_name = validated_data['last_name']
        customer.save()

        return customer

# Login Customer Serializer