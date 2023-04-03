from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

#def index(request):
#    return render(request, 'index.html', context={
#        'who': 'World',
#    })

#def about(request):
#    return render(request, 'about.html')

def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )
