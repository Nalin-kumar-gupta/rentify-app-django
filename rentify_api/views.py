from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .models import Profile
from .serializers import  ProfileSerializer
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import HttpResponse
from .utils import assign_owner_permissions, assign_tenant_permissions
from django.contrib.auth.models import User, Group
from rest_framework import generics
from .models import Profile
from django.contrib.auth import login, authenticate
from django.db import transaction



class RegisterView(APIView):
    def post(self, request_data):
        with transaction.atomic():
            request_user_data = request_data.data
            user = User.objects.create_user(
                username=request_user_data['username'],
                email=request_user_data['email'],
                password=request_user_data['password'],
                is_staff=True
            )
            profile = Profile.objects.create(
                user=user,
                phone_number=request_user_data['phone_number'],
                permanent_address=request_user_data['permanent_address'],
                id_proof=request_user_data.get('id_proof', None),
                profile_photo=request_user_data.get('profile_photo', None),
                role=request_user_data['role']
            )
            self._assign_user_group(profile)

        return HttpResponse("CREATED")
    
    def _assign_user_group(self, profile):
        if profile.role == 'owner':
            group, created = Group.objects.get_or_create(name='Owners')
            if created:
                assign_owner_permissions(group)
        elif profile.role == 'tenant':
            group, created = Group.objects.get_or_create(name='Tenants')
            if created:
                assign_tenant_permissions(group)
        profile.user.groups.add(group)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        authenticate(username=request.data['username'], password=request.data['password'])
        login(request, user)
        profile = Profile.objects.get(user=user)
        response.data['role'] = profile.role
        response.data['id'] = profile.id
        return response

class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)




from rest_framework import generics, pagination
from .models import RealEstateProperty
from .serializers import RealEstatePropertySerializer

class RealEstatePropertyPagination(pagination.PageNumberPagination):
    page_size = 9

class RealEstatePropertyListView(generics.ListAPIView):
    queryset = RealEstateProperty.objects.all()
    serializer_class = RealEstatePropertySerializer
    pagination_class = RealEstatePropertyPagination

class RealEstatePropertyDetailView(generics.RetrieveAPIView):
    queryset = RealEstateProperty.objects.all()
    serializer_class = RealEstatePropertySerializer



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InterestMap
from .serializers import InterestMapSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InterestMap
from .serializers import InterestMapSerializer
from django.shortcuts import get_object_or_404

class CreateInterestMapView(APIView):
    def post(self, request, format=None):
        # Extract userId and propertyId from the request data
        profileId = request.data.get('userId')
        print(profileId)
        propertyId = request.data.get('propertyId')
        print(propertyId)

        # Check if an InterestMap entry already exists for the given userId and propertyId
        existing_interest_map = InterestMap.objects.filter(profile_id=profileId, property_id=propertyId).exists()
        if existing_interest_map:
            return Response({"detail": "InterestMap entry already exists for this user and property."}, status=status.HTTP_200_OK)

        # Create a new InterestMap entry
        profile = get_object_or_404(Profile, id=profileId)
        property = get_object_or_404(RealEstateProperty, id=propertyId)
        data = {'user': profile.user.id, 'profile': profile.id, 'property': property.id, 'email': profile.user.email}
        serializer = InterestMapSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)