from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello django!')


def detail(request, pk):
    msg = '{}번 사진 보여줄게요.'.format(pk)
    return HttpResponse(msg)
