# Create your views here.
from django.shortcuts import render


def index(request):
    query_param = request.GET.get("address", None)
    return render(request, "pages/inspect.html", {"address": query_param})
