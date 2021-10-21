# from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from core.models import TheMain
from referral.utils import generate_ref_code
from user.models import User


class Referral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_balance = models.IntegerField(default=0)
    code = models.CharField(max_length=12, blank=True)
    referred_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="ref_by")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    approve= models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}- {self.code}'

    def get_reffered(self):
        qs = Referral.objects.all()
        my_refs = []
        for reffered in qs:
            if reffered.referred_by == self.user:
                my_refs.append(reffered)
        return my_refs

    def get_referred_balance(self):
        bal = TheMain.objects.all()
        ref_bal = []
        for ref_balance in bal:
            if ref_balance.user == self.user:
                ref_bal.append(ref_balance)
        return ref_bal

    def save(self, *args, **kwargs):
        if self.code == '':
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)
