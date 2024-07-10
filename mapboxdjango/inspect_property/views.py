# Create your views here.
from django.http import HttpResponse


def index(request):
    query_param = request.GET.get("address", None)
    return HttpResponse(f"Inspect Properties @ address: {query_param}")
