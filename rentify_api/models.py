from django.db import models
from django.contrib.auth.models import User
import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/profiles/user_<id>/<filename>
    return f'profiles/user_{instance.user.id}/{filename}'




class Profile(models.Model):
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('tenant', 'Tenant'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, help_text="Role of the user")
    phone_number = models.CharField(max_length=15, unique=True)
    permanent_address = models.TextField(unique=True)
    id_proof = models.FileField(upload_to=user_directory_path)
    profile_photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    

class RealEstateProperty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200, unique=True, help_text="Title of the property listing")
    description = models.TextField(help_text="Detailed description of the property")
    address = models.CharField(max_length=255, unique=True, help_text="Full address of the property")
    city = models.CharField(max_length=100, help_text="City where the property is located")
    state = models.CharField(max_length=100, help_text="State where the property is located")
    zip_code = models.CharField(max_length=20, help_text="Postal code of the property location")
    country = models.CharField(max_length=100, help_text="Country where the property is located")

    property_type = models.CharField(max_length=50, choices=[
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condominium'),
        ('townhouse', 'Townhouse'),
        ('studio', 'Studio'),
        ('loft', 'Loft')
    ], help_text="Type of the property")
    bedrooms = models.PositiveIntegerField(help_text="Number of bedrooms")
    bathrooms = models.PositiveIntegerField(help_text="Number of bathrooms")
    square_feet = models.PositiveIntegerField(help_text="Total area in square feet")
    furnished = models.BooleanField(default=False, help_text="Is the property furnished?")
    pet_friendly = models.BooleanField(default=False, help_text="Is the property pet-friendly?")
    available_from = models.DateField(help_text="Date from which the property is available for rent")
    
    rent_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monthly rent price in USD")
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, help_text="Security deposit amount in USD")
    lease_term = models.CharField(max_length=50, choices=[
        ('month-to-month', 'Month-to-Month'),
        ('6-months', '6 Months'),
        ('12-months', '12 Months'),
        ('24-months', '24 Months')
    ], help_text="Lease term duration")

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owned_properties', help_text="Owner of the property")
    
    contact_name = models.CharField(max_length=100, help_text="Name of the contact person")
    contact_phone = models.CharField(max_length=20, help_text="Phone number of the contact person")
    contact_email = models.EmailField(help_text="Email address of the contact person")
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the property listing was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the property listing was last updated")

    class Meta:
        verbose_name = "Real Estate Property"
        verbose_name_plural = "Real Estate Properties"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.address}, {self.city}"


class InterestMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    property = models.ForeignKey(RealEstateProperty, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)



class Invite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, related_name='sent_invites', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_invites', on_delete=models.CASCADE)
    property = models.ForeignKey(RealEstateProperty, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invite from {self.sender} to {self.recipient} for {self.property.title}"