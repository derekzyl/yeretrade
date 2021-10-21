from datetime import datetime

import pytz
from django.conf import settings

from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from user.models import User
from core.utils import generate_fund_id, generate_invest_id

choice=(
 ('bitcoin','bitcoin'),
('etherium','etherium'),
('BNB','   BNB'),




)

status =(
    ('approved', 'approved'),
    ('cancelled', 'cancelled'),
    ('pending', 'pending'),

)


invest =(
    # ('active', 'active'),
    ('completed', 'completed'),
    ('ongoing', 'ongoing'),

)

method=(
    ('bank', 'bank'),
    ('bitcoin', 'bitcoin'),
    ('etherium', 'etherium'),
    ('BNB', 'BNB'),

)










#TODO: this is to be edited

class TheRef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ref_balance= models.IntegerField(default=0)

class Fund_Account(models.Model):
    fund_id = models.CharField(max_length=6, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_to_fund = models.FloatField(default=0)
    type = models.CharField(choices=choice, default='bitcoin', max_length=10)
    deposit_status = models.CharField(choices=status, default='pending', max_length=10)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.fund_id== '':
            fund_id = generate_fund_id()
            self.fund_id = fund_id
        super().save(*args, **kwargs)



#todo: calculate the returns naturally

class Plans(models.Model):

     plan_name = models.CharField(default=None, max_length=50)
     plan_daily_percentage = models.IntegerField(default=0)
     days_duration = models.IntegerField(default=0)
     minimum_deposit = models.IntegerField(default=0)
     maximum_deposit = models.IntegerField(default=0)
     expected_returns = models.IntegerField(default=0)
     slug = models.SlugField()

     def get_expected_minimum(self):
         return self.minimum_deposit * (self.plan_daily_percentage/100) * self.days_duration

     def get_expected_maximum(self):
         return self.maximum_deposit * (self.plan_daily_percentage/100) * self.days_duration

     def __str__(self):
         return str(self.plan_name)

     def get_absolute_url(self):
        return reverse('core:new-investment', kwargs={'slug': self.slug})




#TODO: we will need to figure out the count down time for the days remaining
class Invest(models.Model):
    invest_id =  models.CharField(max_length=6, blank=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    investment = models.CharField( default='vip', max_length=10)
    invested_amount = models.IntegerField(default=0)
    status = models.CharField(choices=invest, default='ongoing' , max_length=50)
    started = models.DateTimeField(auto_now_add= True)
    time_left = models.DurationField()
    duration = models.IntegerField(default = 7)
    daily_percent =models.IntegerField(default=0)
    timer = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.invest_id == '':
            invest_id = generate_invest_id()
            self.invest_id = invest_id
        super().save(*args, **kwargs)


    def get_profit(self):
        return self.invested_amount * (self.daily_percent/ 100) * self.duration

    def get_expected_return(self):
        return self.get_profit() + self.invested_amount

    def get_absolute_url(self):
        return reverse('core:delete_investment', kwargs={'pk':self.pk})



    def __str__(self):
        return str(self.user)




class TheMain(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    main_balance = models.IntegerField(default=0)
    earning_balance = models.IntegerField(default=0)
    ref_balance= models.IntegerField(default=0)
    invest = models.ForeignKey(Invest, on_delete=models.CASCADE, blank=True, null=True)
    fund = models.ForeignKey(Fund_Account,on_delete=models.CASCADE, blank=True, null=True)








    def __str__(self):
        return str(self.user)





class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_to_withdraw = models.IntegerField(default=0)
    withdrawal_status = models.CharField(choices=status, default='pending', max_length=50)
    method = models.CharField(choices=method, default='bitcoin', max_length=12)

    date_created = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return str(self.user)

# class Referral(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     username = models.CharField(default=None, max_length=50)
#     account_status =models.CharField(default=None, max_length=50)
#     date_registered = models.DateTimeField()
#     user_investment = models.CharField(default=None, max_length=50)
#     invested_status = models.CharField(default=None, max_length=50)
#     referral_bonus = models.CharField(default=None, max_length=50)
#
#     def __str__(self):
#         return str(self.user)
#
#
