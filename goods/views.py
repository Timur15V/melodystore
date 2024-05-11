from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import context

import goods
from goods.models import Products
from goods.models import Subcategories
from goods.models import Categories


def catalog(request, category_slug):

    page = request.GET.get("page", 1)

    if category_slug == "all":
        goods = Products.objects.all()

        paginator = Paginator(goods, 6)
        current_page = paginator.page(int(page))

        context = {"title": "MelodyStore - Каталог", "goods": current_page}

        return render(request, "goods/catalog.html", context)
    else:

        subcategory = Subcategories.objects.filter(category__slug=category_slug)

        context = {
            "title": "MelodyStore - Каталог",
            "subcategory": subcategory,
        }

        return render(request, "goods/category.html", context)


def subcategories(request, category_slug, subcategory_slug):

    page = request.GET.get("page", 1)

    goods = get_list_or_404(
        Products,
        category__slug=subcategory_slug,
    )

    paginator = Paginator(goods, 6)
    current_page = paginator.page(int(page))
    # goods = Products.objects.filter(category__slug=subcategory_slug)

    context = {
        "title": "MelodyStore - Каталог",
        "goods": current_page,
    }
    return render(request, "goods/catalog.html", context)


def product(request, category_slug, subcategory_slug, product_slug):

    product = get_object_or_404(Products, slug=product_slug)

    context = {"product": product}

    return render(request, "goods/product.html", context=context)
