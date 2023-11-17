from django.urls import path

from exchange.views import exchange


app_name = "exchange"

urlpatterns = [
    path("", exchange, name="exchange")
]
