from django import forms


class Contact(forms.Form):
    fullName = forms.CharField(max_length= 10, label='news letter', widget=forms.TextInput(attrs={'placeholder': 'full name'}))
    email_address = forms.EmailField(label='news letter', widget=forms.TextInput(attrs={'placeholder': 'email address'}))
    message = forms.TextInput()


class News(forms.Form):
    email_address = forms.EmailField(label='news letter', widget=forms.TextInput(attrs={'placeholder': 'email address'}))

