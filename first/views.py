from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.views.generic.base import View

from first.models import Account


def index(request):
    return render(request, 'first/index.html')


def about(request):
    return render(request, 'first/about.html')


def faq(request):
    return render(request, 'first/faq.html')


def partners(request):
    return render(request, 'first/partners.html')


class signin(View):
    def get(self, request):
        return render(request, 'first/signin.html')

    def post(self, request):
        user = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=user, password=password)
        login(request, user)
        return redirect('/account/')


class register(View):
    def get(self, request):
        return render(request, 'first/register.html')

    def post(self, request):
        Account.objects.create_user(
            username=request.POST['username'],
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            password=request.POST['pass'],
        )
        return redirect('/signin')


def eventmap(request):
    return render(request, 'first/eventmap.html')


def profile(request):
    return render(request, 'first/account.html')
