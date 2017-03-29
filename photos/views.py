from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello django!')


def detail(request):
    return HttpResponse('detail 뷰 함수')
