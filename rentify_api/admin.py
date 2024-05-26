from django.contrib import admin
from .models import Profile, RealEstateProperty
from django.contrib.admin.sites import AdminSite
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.urls import reverse
from .models import Profile, RealEstateProperty, InterestMap, Invite
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required




from django.contrib import admin
from .models import RealEstateProperty
from django.contrib.auth.models import User


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone_number')
    search_fields = ('user__username', 'role', 'phone_number')
    list_filter = ('role',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            if not request.user.is_superuser:
                kwargs["queryset"] = User.objects.filter(id=request.user.id)
            else:
                kwargs["queryset"] = User.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Profile, ProfileAdmin)



class RealEstatePropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'city', 'state', 'zip_code', 'country', 'owner')
    search_fields = ('title', 'address', 'city', 'state', 'zip_code', 'country', 'owner__username')
    list_filter = ('city', 'state', 'country')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        profile = Profile.objects.get(user=request.user)
        return queryset.filter(owner=profile)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "owner":
            if not request.user.is_superuser:
                profile = Profile.objects.get(user=request.user)
                kwargs["queryset"] = Profile.objects.filter(id=profile.id)
            else:
                kwargs["queryset"] = Profile.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(RealEstateProperty, RealEstatePropertyAdmin)


from django.contrib import admin
from .models import InterestMap, Invite
from .tasks import create_invite

@admin.action(description='Send custom invite to selected profiles')
def send_custom_invite(modeladmin, request, queryset):
    for interest in queryset:
        sender_id = request.user.id
        recipient_id = interest.profile.user.id
        property_id = interest.property.id
        message = f"You are invited to check out the property: {interest.property.title}"
        create_invite.delay(sender_id, recipient_id, property_id, message)

class InterestMapAdmin(admin.ModelAdmin):
    list_display = ('property', 'profile')
    list_filter = ('property',)
    actions = [send_custom_invite]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        profile = Profile.objects.get(user=request.user)
        return queryset.filter(property__owner=profile)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "property":
            if not request.user.is_superuser:
                profile = Profile.objects.get(user=request.user)
                kwargs["queryset"] = RealEstateProperty.objects.filter(owner=profile)
            else:
                kwargs["queryset"] = RealEstateProperty.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(InterestMap, InterestMapAdmin)


class InviteAdmin(admin.ModelAdmin):
    list_display = ('sender', 'property', 'created_at')
    list_filter = ('property',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        profile = Profile.objects.get(user=request.user)
        return queryset.filter(recipient=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "recipent":
            if not request.user.is_superuser:
                profile = Profile.objects.get(user=request.user)
                kwargs["queryset"] = User.objects.filter(id=request.user.id)
            else:
                kwargs["queryset"] = User.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Invite, InviteAdmin)


