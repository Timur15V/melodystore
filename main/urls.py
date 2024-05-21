from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("shipping-and-payment/", views.ship_payment, name="shipping-and-payment"),
    path("contact-info/", views.contact_info, name="contact-info"),
]
