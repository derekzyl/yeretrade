from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .forms import mySignUp
from .models import KYC, Address, Bank, User, VerifyPayment, SignUpForm


# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model= User


    # add_fieldsets=UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'country')})
    # )
    # fieldsets=UserAdmin.add_fieldsets +(
    #     (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'country')}))
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'country', 'approve_broker')



class UserAdmin(admin.ModelAdmin):


    admin.site.register(KYC),
    admin.site.register(Address),
    admin.site.register(Bank),
    admin.site.register(VerifyPayment),
    admin.site.register(SignUpForm),
    admin.site.register(User, CustomAdmin),





