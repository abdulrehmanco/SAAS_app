import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request,*args,**kwargs):
    qs = PageVisits.objects.all()
    queryset = PageVisits.objects.filter(path=request.path)
    my_title='please Just dont give up'
    html_template = 'home.html'
    #path = request.path
    #print('path',path)
    PageVisits.objects.create(path=request.path)
    my_context = {
        "page":my_title,
        "queryset_count":queryset.count(),
        "Random_Percentage":(queryset.count() * 100)/(qs.count() * 50),
        "total_visits":qs.count()
    }

    return render(request,html_template,my_context)

def about(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    queryset = PageVisits.objects.filter(path =request.path)
    try:
        percentage = (queryset.count() * 100)/(qs.count() * 50)
    except:
        percentage = 0,
    my_title='please Just dont give up'
    html_template = 'home.html'
    #path = request.path
    #print('path',path)
    PageVisits.objects.create(path=request.path)
    my_context = {
        "page":my_title,
        "queryset_count":queryset.count(),
        "Random_Percentage":percentage,
        "total_visits":qs.count()
    }

    return render(request,html_template,my_context)