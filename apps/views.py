from django.http import HttpResponse
from . import backend_libs
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.http import Http404

from . import RatingSerializer
from . import CommandeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def dbReq (request):
    return JsonResponse(backend_libs.getCategories())

def prd (request):
    return JsonResponse(backend_libs.getProducts())

def venteprd (request):
    return JsonResponse(backend_libs.getVentesParProduit())

def ventedate (request):
    return JsonResponse(backend_libs.getVenteParDate())

def ventetot (request):
    return JsonResponse(backend_libs.getTotalVente())


class RatingList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = RatingSerializer.RatingSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RatingSerializer.RatingSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommandeList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = CommandeSerializer.CommandeSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommandeSerializer.CommandeSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
