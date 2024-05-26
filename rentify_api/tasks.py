from celery import shared_task
from .models import Invite, RealEstateProperty
from django.contrib.auth.models import User

@shared_task
def create_invite(sender_id, recipient_id, property_id, message):
    sender = User.objects.get(id=sender_id)
    recipient = User.objects.get(id=recipient_id)
    property = RealEstateProperty.objects.get(id=property_id)

    invite = Invite.objects.get_or_create(
        sender=sender,
        recipient=recipient,
        property=property,
        message=message
    )
    return invite.id