from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import View

from core.forms import DepositForm


def deposit(request):

    data={
        'form': DepositForm(),

    }
    return {}
