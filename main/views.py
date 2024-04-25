from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from goods.models import Categories


# Create your views here.
def index(request):

    categories = Categories.objects.all()

    context = {
        "title": "MelodyStore - Главная",
        "content": "Магазин музыкальных инструментов MelodyStore",
        "categories": categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "MelodyStore - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том, какой наш магазин прекрасный и почему вы должны выбрать именно вас",
    }

    return render(request, "main/about.html", context)
