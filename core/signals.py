
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from core.models import Fund_Account, TheMain, TheRef
# from user.models import SignUpForm
from user.models import User


@receiver(post_save, sender=User)
def createmain(sender, instance, created, **kwargs):
    if created:
        TheMain.objects.create(user=instance)


@receiver(post_save, sender=User)
def createref(sender, instance, created, **kwargs):
    if created:
        TheRef.objects.create(user=instance)

# @receiver(post_save, sender=TheMain)
# def createref(sender, instance, created, **kwargs):
#     if instance.fund.deposit_status == 'approved':
#         instance.update()
#
#
#
#

