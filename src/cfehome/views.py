import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

LOGIN_URL = settings.LOGIN_URL

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
Valid_code = 'abc123'
def pw_user_view(request,*args, **kwargs):
    is_allowed = request.session.get("protected_page_allowed") or None
    if request.method == "POST":
        pw_user_sent = request.POST.get("code") or None
        if pw_user_sent == Valid_code:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, 'protected/view.html',{})
    return render(request, 'protected/entry.html',{})

@login_required(login_url=LOGIN_URL)
def user_only_view(request, *args, **kwargs):
    return render(request, "protected/user_only.html" , {})

@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request, *args, **kwargs):
    return render(request, "protected/user_only.html" , {})

 