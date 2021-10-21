from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
from django_countries.fields import CountryField


class User(AbstractUser):
    phone = models.CharField(max_length=15)
    country = CountryField()
    approve_broker = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'




class SignUpForm(models.Model):
    # phoneregex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return f'{self.user.username}'


class KYC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    front_id= models.ImageField(default=None, upload_to='_verify_id')
    back_id = models.ImageField(default=None, upload_to='_verify_id')

    def __str__(self):
        return f'{self.user.username}'



class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    postal_address= models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'



class Bank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50, blank=True)
    account_name = models.CharField(max_length=50, blank=True)
    account_number = models.CharField(max_length=50,blank=True)


    bitcoin_wallet_address = models.CharField(max_length=50, blank=True)
    etherium_wallet_address = models.CharField(max_length=50, blank=True)
    usdt_wallet_address = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return f'{self.user.username}'


class VerifyPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_proof = models.ImageField(default=None, upload_to= '_payment_proof')


    def __str__(self):
        return f'{self.user.username}'