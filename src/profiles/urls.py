from django.urls import path 
from .views import profile_View 


urlpatterns = [
    path('<str:username>/', profile_View),
        
]
