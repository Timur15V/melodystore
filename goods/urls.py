from django.urls import path

from goods import views

app_name = "goods"

urlpatterns = [
    path("<slug:category_slug>/", views.catalog, name="index"),
    path(
        "<slug:category_slug>/<slug:subcategory_slug>/",
        views.subcategories,
        name="subcategories",
    ),
    path(
        "<slug:category_slug>/<slug:subcategory_slug>/<slug:product_slug>/",
        views.product,
        name="product",
    ),
]
