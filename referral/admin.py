from django.contrib import admin

# Register your models here.
from referral.models import Referral


class BrokerAdmin(admin.ModelAdmin):
    admin.site.register(Referral)