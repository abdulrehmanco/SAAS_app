from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

@login_required
def profile_View(request, username=None, *args, **kwargs):
    user = request.user
    print(user.has_perm("auth.add_user"))
    #<app_label (Yahan par auth app hai )>.view_<model_name (Yahan par user model hai)>
    #<app_label>.add<model_name>
    #<app_label>.change<model_name>
    #<app_label>.delete<model_name>
    print(user.has_perm("visits.view_pagevisits"),'user.has_perm("visits.view_pagevisits")')
    # { Waisy he yaha par <app_label> = visits hai .view method aur phir <model_name> = pagevisits lowercase mai }
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    return HttpResponse(f"Hello there my dear {username} - {profile_user_obj.id}- {user.id} - {is_me}")


