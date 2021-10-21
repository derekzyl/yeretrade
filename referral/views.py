import json

from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from core.forms import DepositForm
from core.models import TheMain, Invest, TheRef
from referral.models import Referral


@login_required
def referral_page(request, *args, **kwargs):
    global invest_user, invest_name, invest_amount, invest_timer, main, that, ma, new_invest, new_main
    referral = get_object_or_404(Referral, user=request.user)
    my_ref = referral.get_reffered()
    formd = DepositForm()

    refer_main = []

    for my in my_ref:
        # ref = Ref.objects.get(user=request.user)
        # ref = get_object_or_404(Ref, user=request.user)


        main = TheMain.objects.filter(user=my.user)
        the_main = []
        for ma in main:
            main_balance = f'Main Account Balance: ${ma.main_balance}'
            main_earning = f'Main Earning Balance: ${ma.earning_balance}'
            main_user = f'--MAIN ACCOUNT--   Referred User: {ma.user.first_name} {ma.user.last_name}'

            the_main.append(main_user)
            the_main.append(main_balance)
            the_main.append(main_earning)


        invest = Invest.objects.filter(user=my.user)
        the_invest = []
        for inv in invest:
            invest_user = f'--INVESTMENT--   Referred User :  {inv.user.first_name} {inv.user.last_name}'
            invest_name = f'Investment Name: {inv.investment} PLAN'
            invest_amount = f'Investment Amount: ${inv.invested_amount}'
            invest_return = f'Expected Pay: ${inv.get_expected_return()}'
            invest_timer = f'Payment Date: {inv.timer}'

            the_invest.append(invest_user)
            the_invest.append(invest_name)
            the_invest.append(invest_amount)
            the_invest.append(invest_return)
            the_invest.append(invest_timer)


        refer_main.append(the_main)
        refer_main.append(the_invest)

    context = {
        'ref': refer_main,
        'my_ref': my_ref,
        'referral': referral,
        'formd': formd

    }

    print(f'this is the ref {refer_main}')
    return render(request, 'referral/referral.html', context)




@login_required
def ajax_referral_page(request, *args, **kwargs):
    global invest_user, invest_name, invest_amount, invest_timer, main, that, ma, new_invest, new_main
    referral = get_object_or_404(Referral, user=request.user)
    my_ref = referral.get_reffered()

    refer_main = []

    for my in my_ref:

        main = TheMain.objects.filter(user=my.user)
        the_main = []
        for ma in main:
            main_account = {
                'user': f'{ma.user.first_name} {ma.user.last_name}',
                'main_balance':ma.main_balance,
                'main_earning':ma.earning_balance
            }



            the_main.append(main_account)



        invest = Invest.objects.filter(user=my.user)
        the_invest = []
        for inv in invest:
            investment_account = {
            'invest_id': inv.invest_id,
            'invest_user' : f' {inv.user.first_name} {inv.user.last_name}',
           'invest_name' : inv.investment,
            'invest_amount' : inv.invested_amount,
            'invest_return': inv.get_expected_return(),
           'invest_timer' : inv.timer
            }

            the_invest.append(investment_account)



        main_refer = {
            'the_main' :the_main,
            'the_invest':the_invest
        }
        refer_main.append(main_refer)


    context = {
        'data': refer_main,
     }
    return JsonResponse(context)
    # context = {
    #
    #     'my_ref': my_ref,
    #     'referral': referral
    #
    # }
    #
    # print(f'this is the ref {refer_main}')
    # return render(request, 'referral/referral.html', context)