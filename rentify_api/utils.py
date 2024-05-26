from django.contrib.auth.models import User, Group
from rest_framework import generics
from .models import Profile, InterestMap




# admin.py or another suitable file
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import RealEstateProperty, Invite

def assign_owner_permissions(group):
    # Allow owners to view, edit, and add RealEstateProperty objects
    property_content_type = ContentType.objects.get_for_model(RealEstateProperty)
    property_permissions = Permission.objects.filter(content_type=property_content_type)
    group.permissions.add(*property_permissions)
    
    # Allow owners to view and edit their own profiles
    profile_content_type = ContentType.objects.get_for_model(Profile)
    profile_permissions = Permission.objects.filter(content_type=profile_content_type, codename__in=['view_profile', 'change_profile'])
    group.permissions.add(*profile_permissions)

    interest_content_type = ContentType.objects.get_for_model(InterestMap)
    interestmap_permissions = Permission.objects.filter(content_type=interest_content_type)
    group.permissions.add(*interestmap_permissions)

    invite_content_type = ContentType.objects.get_for_model(Invite)
    invite_permissions = Permission.objects.filter(content_type=invite_content_type, codename__in=['view_invite', 'delete_invite'])
    group.permissions.add(*invite_permissions)



def assign_tenant_permissions(group):
    # Allow tenants to view and edit their own profiles
    profile_content_type = ContentType.objects.get_for_model(Profile)
    profile_permissions = Permission.objects.filter(content_type=profile_content_type, codename__in=['view_profile', 'change_profile'])
    group.permissions.add(*profile_permissions)

    invite_content_type = ContentType.objects.get_for_model(Invite)
    invite_permissions = Permission.objects.filter(content_type=invite_content_type, codename__in=['view_invite', 'delete_invite'])
    group.permissions.add(*invite_permissions)