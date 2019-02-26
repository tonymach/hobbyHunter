
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from transactions.encryptSchemes import livingDead as lD
from transactions.transSchemes import voodooDoctor as vD
import json
from search.QueryFuncs import pageFuncs

from misc.funcs import ajaxResponse
w = HttpResponse("Works!")
x = HttpResponse("Kinda works!")
from django.contrib.auth import get_user_model
User = get_user_model()

# AJAX

def RegisterAjax(request):
    error=False
    try:
        email = request.POST.get('user')
        password = request.POST.get('pass')
        user = User.objects.create_user(email, password)
        login(request,user)
    except:
        error = True

    return ajaxResponse(error)


def LoginAjax(request):
    error = False
    email = request.POST.get('user')
    password = request.POST.get('pass')
    user = authenticate(email=email, password=password)
    print(user)
    if user is not None:
        login(request, user)
    else:
        error = True
    return ajaxResponse(error)


# REGULAR

def Register(request):
    email = request.POST.get('user')
    password = request.POST.get('pass')
    user = User.objects.create_user(email, password)
    login(request,user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def Login(request):
    email = request.POST.get('user')
    password = request.POST.get('pass')
    user = authenticate(email=email, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie("login_"+lD.Zombie.hash(email),"banana")
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def Logout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def Authorize(request):
    response_data = {}

    password = request.POST.get('pass')
    email = request.user.email

    user = authenticate(email=email, password=password)
    if user is not None:
        response_data['result'] = 'success'
    else:
        response_data['result'] = 'error'
    return HttpResponse(
        json.dumps(response_data),
    content_type="application/json"
        )


def MerchantLogin(request):
    email = request.POST.get('user')
    password = request.POST.get('pass')
    user = authenticate(email=email, password=password)
    print(email)
    if user is not None:
        login(request, user)
        return render(request, 'merchant/index.html')
        response.set_cookie("login_"+lD.Zombie.hash(email),"banana")

    else:
        response = redirect(request.META.get('HTTP_REFERER'))
        response.set_cookie("login_"+lD.Zombie.hash(email),"1")
    return response


def MerchantRegister(request):
    email = request.POST.get('user')
    password = request.POST.get('pass')
    phone = request.POST.get('phone')
    user = User.objects.create_user(email, password)
    user.accType = 'M'
    # user.phone_number = phone
    user.save()
    login(request,user)
    return HttpResponseRedirect('/merchant/')


def postAPage(request):
    response_data = {}
    print(request.FILES)
    title = request.POST.get('title')
    description = request.POST.get('description')
    averageCost = request.POST.get('averageCost')
    mainImage = request.FILES['mainImage']
    try:
        if pageFuncs.creation.post(request.user.email, title, description, averageCost, mainImage):
            response_data['result'] = 'success'

        else:
            response_data['result'] = 'error'

    except:
        response_data['result'] = 'error'

    return HttpResponse(
            json.dumps(response_data),
        content_type="application/json"
            )


def addSession(request):
    """
    Submits a schedule, endpoint and schedule
    """
    merchant = request.user.email
    date = request.POST.get('datetime')
    pageId = request.POST.get('pageId')
    session = vD.createId()
    spots = request.POST.get('spots')

    response = vD.createPageSchedule(merchant,date,pageId,session,spots)
    return response
