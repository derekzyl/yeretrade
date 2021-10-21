# from datetime import datetime, timedelta
import json
from datetime import datetime, timedelta

import pytz
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import View

from core.forms import DepositForm, WithdrawForm, InvestForm
from core.models import Plans, Fund_Account, Withdrawal, TheMain, \
    Invest, TheRef
from user.forms import SignForm, KycForm, AddressForm, BankForm
from user.models import KYC, SignUpForm, Address, Bank, VerifyPayment


class dashboard(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        the = get_object_or_404(TheMain, user=self.request.user)
        formd = DepositForm()

        context = {
            'formd': formd,
            'the': the,

        }
        return render(self.request, 'core/dashboard.html', context)


class depositHistory(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            deposits = Fund_Account.objects.filter(user=self.request.user).order_by('-date_created')
            formd = DepositForm()

            context = {
                'formd': formd,
                'deposits': deposits
            }
            return render(self.request, 'core/depositeHistory.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, 'you dont have an active deposit')


@login_required()
def earning(request):
    obj = get_object_or_404(TheMain, user=request.user)
    invest = Invest.objects.filter(user=request.user)
    formd = DepositForm()
    context = {
        'formd': formd,
        'obj': obj,
        'invest': invest
    }

    return render(request, 'core/earning.html', context)


class Fund(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        account = Fund_Account.objects.filter(user=self.request.user)
        formd = DepositForm()

        main = get_object_or_404(TheMain, user=self.request.user)
        verifyPay = VerifyPayment.objects.filter(user=self.request.user)
        deposits = Fund_Account.objects.filter(user=self.request.user).order_by('-date_created')
        context = {
            'formd': formd,

            'account': account,
            'main': main,
            'verifyPay': verifyPay,
            'deposits': deposits
        }
        return render(self.request, 'core/fund_account.html', context)

    # def post(self, *args, **kwargs):
    #
    #     the = get_object_or_404(TheMain, user=self.request.user)
    #
    #     if self.request.is_ajax and self.request.method == 'POST':
    #         form = DepositForm(self.request.POST)
    #         forma = ProofForm(self.request.POST, self.request.FILES)
    #
    #
    #
    #         if form.is_valid():
    #             if not form.cleaned_data.get('amount_to_fund') <= 0:
    #
    #                 account = form.save(commit=False)
    #                 account.user = self.request.user
    #                 account.save()
    #                 messages.success(self.request, 'funds request received proceed to submit evidence of payment')
    #                 amount_to = Fund_Account.objects.filter(user=self.request.user, deposit_status__in=['approved'])
    #                 for fund in amount_to:
    #                     approved = fund.amount_to_fund
    #                     the.main_balance += approved
    #                     the.save()
    #
    #                 return redirect('core:fund')
    #
    #
    #             return redirect('core:dashboard')
    #         if forma.is_valid():
    #             accounta = forma.save(commit=False)
    #             accounta.user = self.request.user
    #             accounta.save()
    #             messages.success(self.request, 'proof of payment received and is being processed')
    #             return redirect('core:dashboard')


class Setting(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        bal = get_object_or_404(TheMain, user=self.request.user)
        form_sign = SignForm()
        form_kyc = KycForm()
        form_ad = AddressForm()
        form_bank = BankForm()
        formd = DepositForm()
        context = {
            'formd': formd,
            'form_ad': form_ad,
            'form_bank': form_bank,
            'form_kyc': form_kyc,
            'form_sign': form_sign,
            'bal': bal
        }

        # kyc = KYC.objects.get(user=self.request.user)
        # if kyc.exists():
        #     context.update(
        #         {'kyc': kyc[0]}
        #     )
        #
        # sign = SignUpForm.objects.get(user=self.request.user)
        # if sign.exists():
        #     context.update({
        #         'sign': sign[0]})
        #
        # ad = Address.objects.get(user=self.request.user)
        # if ad.exists():
        #     context.update({
        #         'ad': ad[0]
        #     })

        # bank = get_object_or_404(Bank, user=self.request.user)
        #
        # context.update({
        #         'bank': bank
        #     })

        return render(self.request, 'core/setting.html', context)

    def post(self, *args, **kwargs):

        if self.request.method == 'POST':
            sign = SignUpForm.objects.filter(user=self.request.user).first()
            kyc = KYC.objects.filter(user=self.request.user).first()

            ad = Address.objects.filter(user=self.request.user).first()
            bank = Bank.objects.filter(user=self.request.user).first()

            if sign:
                form_sign = SignForm(self.request.POST, instance=sign)
            else:
                form_sign = SignForm(self.request.POST)

            if kyc:
                form_kyc = KycForm(self.request.POST, self.request.FILES, instance=kyc)

            else:
                form_kyc = KycForm(self.request.POST, self.request.FILES)

            if bank:
                form_bank = BankForm(self.request.POST, instance=bank)
            else:
                form_bank = BankForm(self.request.POST)

            if ad:
                form_ad = AddressForm(self.request.POST, instance=ad)
            else:
                form_ad = AddressForm(self.request.POST)

            print(form_sign)
            print(form_kyc)
            print(form_ad)
            print(form_bank)

            if form_bank.is_valid():
                account = form_bank.save(commit=False)

                account.user = self.request.user
                account.save()
                messages.success(self.request, 'account details saved successfully')
                return redirect('core:setting')

            if form_ad.is_valid():
                accounta = form_ad.save(commit=False)
                accounta.user = self.request.user
                accounta.save()
                messages.success(self.request, 'bio data updated')
                return redirect('core:setting')

            if form_sign.is_valid():
                accountb = form_sign.save(commit=False)
                accountb.user = self.request.user
                accountb.save()
                messages.success(self.request, 'details saved successfully')
                return redirect('core:setting')

            if form_kyc.is_valid():
                accountc = form_kyc.save(commit=False)
                accountc.user = self.request.user
                accountc.save()
                messages.success(self.request, 'kyc updated successfully')
                return redirect('core:setting')

            messages.error(self.request, 'seems like you inputed an incorrect data')
            return redirect('core:setting')


@login_required()
def myInvestment(request):
    formd = DepositForm()
    invest = Invest.objects.filter(user=request.user).order_by("-started")
    countdown = []
    for inv in invest:
        timer = str(inv.timer)

        countdown += [timer]

    context = {
        'formd': formd,
        'invest': invest,
        'countdown': json.dumps(countdown)
    }
    return render(request, 'core/myinvestment.html', context)


@login_required()
def ajaxInvestment(request):
    invest = Invest.objects.filter(user=request.user).order_by("-started")
    formd = DepositForm()
    all_invest = []
    for inv in invest:
        ajaxInvest = {
            'id': inv.id,
            'investment': inv.investment,
            'status': inv.status,
            'invested_amount': inv.invested_amount,
            'duration': inv.duration,
            'started': inv.started,
            'get_profit': inv.get_profit(),
            'get_expected_return': inv.get_expected_return(),
            'timer': inv.timer,
            'invest_id': inv.invest_id
        }
        all_invest.append(ajaxInvest)

    context = {
        'data': all_invest,

    }

    return JsonResponse(context)


class NewInvestment(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        formd = DepositForm()
        name = get_object_or_404(Plans, slug=kwargs['slug'])
        themain = get_object_or_404(TheMain, user=self.request.user)
        form = InvestForm()
        context = {
            'formd': formd,
            'name': name,
            'themain': themain,
            'form': form
        }
        return render(self.request, 'core/newinvestment.html', context)

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            fund = Fund_Account.objects.filter(user=self.request.user)
            form = InvestForm(self.request.POST)
            plan = get_object_or_404(Plans, slug=[kwargs['slug']])

            if form.is_valid():
                if not form.cleaned_data.get('invested_amount') <= 0:
                    newform = form.save(commit=False)
                    newform.user = self.request.user
                    newform.save()


@login_required()
def purchasePlan(request):
    formd = DepositForm()
    context = {
        'formd': formd,
        'plans': Plans.objects.all()
    }

    return render(request, 'core/purchaseplane.html', context)


class Withdraw(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        formd = DepositForm()
        form = WithdrawForm()
        withdraw = Withdrawal.objects.filter(user=self.request.user)
        bank = Bank.objects.filter(user=self.request.user)
        context = {
            'formd': formd,
            'form': form,
            'withdraw': withdraw,
            # 'bank': bank
        }
        return render(self.request, 'core/withdraw.html', context)

    def post(self, *args, **kwargs):

        if self.request.method == 'POST':
            main = get_object_or_404(TheMain, user=self.request.user)

            form = WithdrawForm(self.request.POST or None)
            if form.is_valid():

                foo = form.cleaned_data.get('amount_to_withdraw')
                fo = form.cleaned_data.get('method')

                if foo < main.main_balance or foo == main.main_balance or foo < main.earning_balance or foo == main.earning_balance or foo < (
                        main.main_balance + main.earning_balance):

                    ford = form.save(commit=False)
                    ford.user = self.request.user
                    ford.save()
                    # subject = 'withdrawals from www.coinminfx.com'
                    # message = f'dear {self.request.user.username} you have requested the withdrawal of ${foo} using {fo} your request is being processed copyright www.coinminfx.com'
                    # sent_from = settings.DEFAULT_FROM_EMAIL
                    # send_to = [self.request.user.email]
                    #
                    # send_mail(
                    #     subject,
                    #     message ,
                    #     sent_from,
                    #     send_to
                    # )

                    messages.success(self.request, 'withdrawal request received and is being processed')
                    return redirect('core:dashboard')
                else:
                    messages.success(self.request, 'seems like your balance is insufficient')
                    return redirect('core:fund')

                return redirect('core:withdraw')


def collect(request, *args, **kwargs):
    global the_started, the_timer, get_expected_return
    dura = request.POST.get('duration')

    timeduration = - timedelta(days=int(dura))
    timer = datetime.now() + timedelta(days=int(dura))

    if request.method == 'POST':
        main = get_object_or_404(TheMain, user=request.user)

        invested = Invest.objects.filter(user=request.user)
        for inv in invested:
            the_started = inv.started
            the_timer = inv.timer
            get_expected_return = inv.get_expected_return()

        form = InvestForm(request.POST or None)
        if form.is_valid():
            id = request.POST.get("id")
            # invested = get_object_or_404(Invest, pk=id)

            invested_amount = form.cleaned_data.get('invested_amount')

            plan_name = request.POST.get('plan_name')
            daily_percent = request.POST.get('daily_percent')
            min = request.POST.get('minimum')
            max = request.POST.get("maximum")

            duration = dura
            print(min)

            invest = Invest(user=request.user,
                            investment=plan_name,
                            duration=duration,
                            daily_percent=daily_percent,
                            invested_amount=invested_amount,
                            time_left=timeduration,
                            timer=timer)
            if main.main_balance < invested_amount:
                messages.info(request, 'seems like your balance is insufficient')
                return redirect('core:fund')
            elif int(min) > int(invested_amount):
                messages.info(request, 'seems like you have not met mininimum deposit for this plan')
                return redirect("core:purchase-plan")
            else:
                invest.save()

                main.main_balance -= invested_amount
                # if the_started  == the_timer or  the_started > the_timer:
                # main.earning_balance += get_expected_return
                # main.earning_balance += invested_amount
                main.save()
                messages.info(request, 'invested amount received')

                messages.info(request, 'main account updated')

        return redirect('core:dashboard')


def delete_investment(request):
    main = get_object_or_404(TheMain, user=request.user)
    if request.is_ajax and request.method == 'POST':

        id = request.POST.get('pk')
        invest = get_object_or_404(Invest, pk=id)

        print(f'this is invest {invest}')

        if invest.started != invest.timer and invest.started < invest.timer:
            main.main_balance += invest.invested_amount
            main.save()
            messages.warning(request, 'investment cancelled and your main account has been updated')
        else:
            messages.error(request, 'completed investment deleted')
        invest.delete()
        context = {
            'data': id
        }

        return JsonResponse(context)


def fund_account(request):
    get_object_or_404(TheMain, user=request.user)

    if request.is_ajax:
        form = DepositForm(request.POST)

        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            # messages.success(request, 'funds request received proceed to submit evidence of payment')
            # amount_to = Fund_Account.objects.filter(user=request.user, deposit_status__in=['approved'])
            # for fund in amount_to:
            #     approved = fund.amount_to_fund
            #     the.main_balance += approved
            #     the.save()

            return JsonResponse({
                'amount': account.amount_to_fund,
                'type': account.type,
                'url': '/core/fund',
                'succeed': True})


def comfirm_payment(request):
    # verify= VerifyPayment.objects.filter(user= request.user)
    if request.method == 'POST':
        img = request.FILES.get('file')
        verify = VerifyPayment.objects.create(
            user=request.user,
            upload_proof=img
        )
        verify.save()
    return HttpResponse()
