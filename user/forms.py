from django import forms
from django.contrib.auth.decorators import login_required

from django.forms import Textarea, DateInput, TextInput
from django.shortcuts import render
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from referral.models import Referral
from user.models import Address, SignUpForm, Bank, KYC, VerifyPayment, User

from allauth.account.forms import SignupForm


class mySignUp(SignupForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'First name'
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Last name'
    }))
    country = CountryField(blank_label='select country').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))
    phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Phone number'
    }))

    # def save(self,  request):
    #     user = super(mySignUp, self).save(request)
    #
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.country = self.cleaned_data['country']
    #     user.phone = self.cleaned_data['phone']
    #     user.save()
    #     print(f'this is the user {user}')
    #     return user

    def save(self, request):
        referral_id = request.session.get('ref_profile')
        print(f'this is login{referral_id}')
        if referral_id is not None:
            recommended_by_profile = Referral.objects.get(id=referral_id)
            user = super(mySignUp, self).save(request)

            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.country = self.cleaned_data['country']
            user.phone = self.cleaned_data['phone']
            user.save()

            registered_user = User.objects.get(id=user.id)
            registered_profile = Referral.objects.get(user=registered_user)
            registered_profile.referred_by = recommended_by_profile.user
            registered_profile.save()
            print(f'this is the user {user}')
            print(f'this is the the {user.id}')

            return user
        else:

            user = super(mySignUp, self).save(request)

            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.country = self.cleaned_data['country']
            user.phone = self.cleaned_data['phone']
            user.save()
            print(f'this is the user {user}')
            return user


def referred(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    print(f'coded code {code}')
    try:
        referral = Referral.objects.get(code=code)
        request.session['ref_profile'] = referral.id
        print('id', referral.id)
    except:
        pass
    print(request.session.get_expiry_age())
    return render(request, 'homepage/index.html', {})


class SignForm(forms.ModelForm):
    class Meta:
        model = SignUpForm

        fields = ['birth_date']
        widgets = {

            'birth_date': DateInput(attrs={
                'placeholder': 'birth_date',
                'type': 'date'
            })
        }


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank

        fields = ['bank_name','account_name', 'account_number' , 'bitcoin_wallet_address', 'usdt_wallet_address', 'etherium_wallet_address']
        widgets = {
            'bank_name': TextInput(attrs={
                'placeholder': 'bank name'

            }),

            'account_name': TextInput(attrs={
                'placeholder': 'account name'

            }),
            'account_number': TextInput(attrs={
                'placeholder': 'account number'

            }),
            'bitcoin wallet address': TextInput(attrs={
                'placeholder': 'bitcoin  address'

            }),
            'usdt_wallet_address': TextInput(attrs={
                'placeholder': 'usdt  address'

            }),


            'etherium_wallet_address': TextInput(attrs={
                'placeholder': 'ethereum  address'

            })
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address', 'postal_address']
        widgets = {
            'address': TextInput(attrs={
                'placeholder': 'address'

            }),
            'postal_address': TextInput(attrs={
                'placeholder': 'postal address'

            })
        }


class KycForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = ['front_id', 'back_id']


