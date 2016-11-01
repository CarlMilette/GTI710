from django.http import HttpResponse
from apps import backend_libs
from django.http import JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def dbReq (request):
    return JsonResponse(backend_libs.getCategories())

def prd (request):
    return JsonResponse(backend_libs.getProducts())