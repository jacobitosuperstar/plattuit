from django.shortcuts import render, redirect

# Create your views here.

from django.contrib import messages
from django.contrib.auth import logout
from account.forms import (
    RegistrationForm,
)

# Si voy a usar la vista de login
# from django.contrib.auth import authenticate
# from account.forms import AccountAuthenticationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('raw_password')
            account = form.save()
            login(request, account)
            return redirect('store')
        else:
            context = {
                'form': form,
            }

    else:
        # GET request
        form = RegistrationForm()
        context = {
            'form': form,
        }
    template = 'account/register.html'
    return render(request, template, context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Come Back Soon!!!')
    return redirect('store')
