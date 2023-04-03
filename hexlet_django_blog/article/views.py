from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):

    def get(self, request):
        return HttpResponse('article')


#name = 'article'

#def index(request):
#    return HttpResponse('article')
#    return render(request, 'article/index.html', context={'name': name})
