from django.contrib import admin

# Register your models here.
from homepage.models import Transaction, Withdrawal, Blog, TeamMembers, TopInvestor, Comment, Slider


#Blog,

class BrokerAdmin(admin.ModelAdmin):
    admin.site.register(Blog)
    admin.site.register(Transaction)
    admin.site.register(Withdrawal)
    admin.site.register(TopInvestor)
    admin.site.register(TeamMembers)
    admin.site.register(Comment)
    admin.site.register(Slider)