from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import JsonResponse
from playlist.models import Playlist

def main(request):
    like = 0
    like = like + 1
    context = {
        "land_type":"about",
        "name": "arsen",
    }
    return render(request, "index.html", context)
    
def about(request):
    context = {
    }
    return render(request, "playlist.html", context)

def sign_in(request):
    context = {
    }
    return render(request, "sign_in.html", context)
    
def reg_user(request):
    name = request.GET.get("mail")
    Playlist.objects.create(name=name)
    data = {
    }
    return JsonResponse(data)