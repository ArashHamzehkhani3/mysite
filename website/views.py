from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return HttpResponse("<b><h3>Home page</h3></b>")


def about(request):
    return HttpResponse("<h3>about us</h3>")
