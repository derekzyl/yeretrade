from django import forms

from core.models import Fund_Account, Withdrawal,  Invest


class DepositForm(forms.ModelForm):
    class Meta:
        model= Fund_Account
        fields = ['amount_to_fund', 'type']

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields=['amount_to_withdraw', 'method']


class InvestForm(forms.Form):
    invested_amount = forms.IntegerField( label='input the amount ')


    # class Meta:
    #     model = Invest
    #     fields = ['invested_amount']
    #
