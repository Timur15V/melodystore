from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginFrom, UserRegistrationForm


# Create your views here.
def login(request):

    if request.method == "POST":
        form = UserLoginFrom(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginFrom()

    context = {"title": "MelodyStore - Авторизация", "form": form}
    return render(request, "users/login.html", context=context)


def registration(request):

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "MelodyStore - Регистрация", "form": form}
    return render(request, "users/registration.html", context=context)


def profile(request):
    context = {"title": "MelodyStore - Профиль"}
    return render(request, "users/profile.html", context=context)


def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))
