from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rentify_api.models import Profile, RealEstateProperty
from faker import Faker
# from django.core.files.base import ContentFile
import random
from django.contrib.auth.models import User, Group
from rentify_api.utils import assign_owner_permissions, assign_tenant_permissions
from django.db import transaction


class Command(BaseCommand):
    help = 'Generate fake data for users, profiles, and properties'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate random users and profiles
        for _ in range(100):
            with transaction.atomic():
                try:
                    user = User.objects.create_user(
                        username=fake.user_name(),
                        email=fake.email(),
                        password='password123',
                        is_staff=True
                    )
                    role = random.choice(['owner', 'tenant'])

                    # Create a temporary file for id_proof and profile_photo
                    # id_proof_file = ContentFile(fake.text(), name=f'{user.username}_id_proof.pdf')
                    # profile_photo_file = ContentFile(fake.image(), name=f'{user.username}_profile_photo.jpg')

                    profile = Profile.objects.create(
                        user=user,
                        role=role,
                        phone_number=fake.phone_number(),
                        permanent_address=fake.address()
                        # id_proof=id_proof_file,
                        # profile_photo=profile_photo_file
                    )
                    self._assign_user_group(profile)
                    if role == 'owner':
                        self.create_fake_properties(profile)


                except:
                    pass

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data'))

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

    def create_fake_properties(self, owner_profile):
        fake = Faker()
        for _ in range(random.randint(1, 10)):  
            RealEstateProperty.objects.create(
                title=fake.sentence(nb_words=6),
                description=fake.paragraph(nb_sentences=5),
                address=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                zip_code=fake.zipcode(),
                country=fake.country(),
                property_type=random.choice(['apartment', 'house', 'condo', 'townhouse', 'studio', 'loft']),
                bedrooms=random.randint(1, 5),
                bathrooms=random.randint(1, 3),
                square_feet=random.randint(500, 5000),
                furnished=fake.boolean(),
                pet_friendly=fake.boolean(),
                available_from=fake.date_this_year(),
                rent_price=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
                security_deposit=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
                lease_term=random.choice(['month-to-month', '6-months', '12-months', '24-months']),
                owner=owner_profile,
                contact_name=owner_profile.user.username,
                contact_phone=owner_profile.phone_number,
                contact_email=owner_profile.user.email
            )
