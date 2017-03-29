from django.shortcuts import render
from django.http import HttpResponse

from .models import Photo


# root\hello/$
def hello(request):
    return HttpResponse('Hello django!')


# root\photos\$
def detail(request, pk):
    photo = Photo.objects.get(pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))
