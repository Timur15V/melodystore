from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import context
from traitlets import default

import goods
from goods.models import Products
from goods.models import Subcategories
from goods.models import Categories
from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get("page", 1)

    on_sale = request.GET.get("on_sale", None)

    order_by = request.GET.get("order_by", None)

    query = request.GET.get("q", None)

    if category_slug == "all":

        goods = Products.objects.all()

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)

        paginator = Paginator(goods, 6)
        current_page = paginator.page(int(page))

        context = {
            "title": "MelodyStore - Каталог",
            "goods": current_page,
            "slug_url": category_slug,
        }

        return render(request, "goods/catalog.html", context)
    elif query:

        goods = q_search(query)

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)

        paginator = Paginator(goods, 6)
        current_page = paginator.page(int(page))

        context = {
            "title": "MelodyStore - Каталог",
            "goods": current_page,
            "slug_url": category_slug,
        }

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

    on_sale = request.GET.get("on_sale", None)

    order_by = request.GET.get("order_by", None)

    goods = Products.objects.filter(category__slug=subcategory_slug)
    # goods = get_list_or_404(
    #     Products,
    #     category__slug=subcategory_slug,
    # )

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 6)
    current_page = paginator.page(int(page))
    # goods = Products.objects.filter(category__slug=subcategory_slug)

    context = {
        "title": "MelodyStore - Каталог",
        "goods": current_page,
        "category_slug": category_slug,
        "subcategory_slug": subcategory_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, category_slug, subcategory_slug, product_slug):

    product = get_object_or_404(Products, slug=product_slug)

    context = {"title": f"MelodyStore - {product.name}", "product": product}

    return render(request, "goods/product.html", context=context)
