from django.contrib import admin
from .models import Fund_Account, Plans, Withdrawal, TheMain, Invest


# Register your models here.


class BrokerAdmin(admin.ModelAdmin):
    admin.site.register(Plans)
    admin.site.register(Fund_Account)
    admin.site.register(Invest)
    admin.site.register(Withdrawal)
    admin.site.register(TheMain)



