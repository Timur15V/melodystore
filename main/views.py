from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from goods.models import Categories


# Create your views here.
def index(request):

    context = {
        "title": "MelodyStore - Главная",
        "content": "Магазин музыкальных инструментов MelodyStore",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "MelodyStore - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том, какой наш магазин прекрасный и почему вы должны выбрать именно вас",
    }

    return render(request, "main/about.html", context)


def ship_payment(request):
    context = {
        "title": "MelodyStore - Доставка и оплата",
        "content": "Доставка и оплата",
    }

    return render(request, "main/ship_payment.html", context)


def contact_info(request):
    context = {
        "title": "MelodyStore - Контактная информация",
        "content": "Контактная информация",
    }

    return render(request, "main/contact_info.html", context)
