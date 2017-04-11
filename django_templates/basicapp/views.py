from django.shortcuts import render
from basicapp.forms import UserForm, UserProfileInfoForm
#for login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    context_dict = {'text':"helloworld", 'number':100, 'text2':'lala heloe lala ce mai faci gica plm de fraier'}
    return render(request, 'basicapp/index.html',context_dict)

def other(request):
    return render(request,'basicapp/other.html')

def url_templates(request):
    return render(request,'basicapp/url_templates.html')


def register(request):

    register = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            #if "profile_pic" in request.FILES:
                #profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            register = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,"basicapp/registration.html",
                    {"user_form":user_form, "profile_form":profile_form, "register":register})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user  = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("SOMEONE LOGED IN AND FAILED")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, "basicapp/login.html",{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def special(request):
    return HttpResponse("YOU CAN SEE THIS PAGE ONLY IF YOU ARE LOGGED IN")
