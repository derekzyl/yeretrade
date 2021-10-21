from django.urls import path, re_path

from referral.views import referral_page, ajax_referral_page
from .views import purchasePlan, NewInvestment, Fund, myInvestment, depositHistory, earning, \
    Setting, dashboard, Withdraw, collect, delete_investment, ajaxInvestment, fund_account, comfirm_payment

app_name='core'
urlpatterns = [
    path('', dashboard.as_view(), name='dashboard'),
    path('setting', Setting.as_view(), name='setting'),
    path('withdraw', Withdraw.as_view(), name='withdraw'),
    # path('referral', referral, name='referral'),


    path('purchase/<slug:slug>', NewInvestment.as_view(), name='new-investment'),
    path('purchase', purchasePlan, name='purchase-plan'),
    path('earning', earning, name='earning'),
    path('deposit-history', depositHistory.as_view(), name='deposit-history'),
    path('fund', Fund.as_view(), name='fund'),
    path('my-investment', myInvestment, name='my-investment'),


    path('collect', collect, name='collect'),

    path('referral', referral_page, name='referral'),
    path('ajax-referral', ajax_referral_page, name='ajax-referral'),
    path('ajax-investment', ajaxInvestment, name='ajax-investment'),

    # re_path(r'^delete/(?P<pk>[0-9]+)/$', delete_investment, name='delete_investment'),

    path('delete-investment', delete_investment, name='delete_investment'),
    path('fund-account', fund_account, name='fund-account'),
    path('comfirm-payment', comfirm_payment, name='comfirm-payment'),

]

