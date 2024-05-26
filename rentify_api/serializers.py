from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'role', 'phone_number', 'permanent_address', 'id_proof', 'profile_photo')


from rest_framework import serializers
from .models import RealEstateProperty

class RealEstatePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateProperty
        fields = '__all__'


# serializers.py
from rest_framework import serializers
from .models import InterestMap

class InterestMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestMap
        fields = ['user', 'profile', 'property', 'email']