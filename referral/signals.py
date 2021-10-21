# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from referral.models import Referral
from user.models import User


@receiver(post_save, sender=User)
def create_referral(sender, instance , created, *args, **kwargs):
    if created:
        Referral.objects.create(user=instance)



