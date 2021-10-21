from django.urls import path

from .views import referral_page
from user.forms import referred

urlpatterns = [
    path('<str:ref_code>', referred, name='referrals'),

]


