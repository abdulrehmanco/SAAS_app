from django.contrib import admin 
from django.urls import path , include
from auth import views as auth_views
from .views import home_page_view , pw_user_view, user_only_view, staff_only_view 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('profiles.urls')),
    path('',home_page_view ,name='home'),
    path("login/",auth_views.login_set),
    path("register/",auth_views.register_set),
    path("protected/",pw_user_view),
    path("protected/user_only",user_only_view),
    path("protected/staff_only",staff_only_view),
    
]
