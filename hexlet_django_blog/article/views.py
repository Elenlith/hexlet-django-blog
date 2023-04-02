from django.shortcuts import render
from django.http import HttpResponse

name = 'article'

def index(request):
#    return HttpResponse('article')
    return render(request, 'article/index.html', context={'name': name})
