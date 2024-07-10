from django.urls import path

from .views import index

app_name = "inspect_property"

urlpatterns = [
    path("search", index, name="search"),
]
