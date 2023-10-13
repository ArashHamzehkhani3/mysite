from django.http import HttpResponse
from django.http import JsonResponse


def http_test(request):
    return HttpResponse("<b><h3>Hello world from django</h3></b>")


def json_test(request):
    return JsonResponse({'name':'arash'})