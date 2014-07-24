# coding: utf-8
from tenant_schemas.utils import remove_www_and_dev
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from django.shortcuts import render

def auth_login(request):
    # Documentação de autenticação na url abaixo:
    # https://docs.djangoproject.com/en/dev/topics/auth/default/
    context = {'hostname': remove_www_and_dev(request.get_host().split('.')[0])}

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'customers/login.html', context)
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            return render(request, 'customers/login.html', context)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def main(request):
    context = {'hostname': remove_www_and_dev(request.get_host().split('.')[0])}
    return render(request, 'customers/dashboard.html', context)