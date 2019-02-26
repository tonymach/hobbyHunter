from django.shortcuts import render
from django.http import HttpResponse
from transactions.encryptSchemes import livingDead as lD
from transactions.transSchemes import voodooDoctor as vD

from misc import funcs
from misc.funcs import ajaxResponse
from transactions.models import Schedule

from django.contrib.auth import get_user_model
User = get_user_model()


from datetime import datetime

# Create your views here.

w = HttpResponse('works!')

def index(request):
    return w


def zombie(request):
    if not User.objects.filter(email='A'):
        funcs.TryMe.put('programming')
        email = 'A'
        password = 'aomg2000'
        phone = '6474541564'
        user = User.objects.create_user(email, password)
        user.accType = 'M'
        # user.phone_number = phone
        user.save()
        login(request,user)
        user = User.objects.create_user('x@b.ca', 'a')
        user.save()
        return HttpResponse('Done!')
    return w


def frankenstein(request):
    return w

def voodooDoctor(request):
    return HttpResponse(vD.create('bana@n.a','banana'))



def createPageSchedule(request):

    error = False
    already = False
    merchant = request.GET.get('merchant')
    date = request.GET.get('datetime')
    pageId = request.GET.get('pageId')


    if not Schedule.objects.filter(pageId=pageId):
        schedule = Schedule.objects.create(pageId=pageId,datetime = date)
        try:
            schedule.save()
        except:
            error = True
    else:
        already = True
    return ajaxResponse(error,already)

def book(request):
    merchant = request.POST.get('merchant')
    sessionId = request.POST.get('sessionId')
    if request.user.is_authenticated():
        vD.book(request.user.email, merchant, sessionId)
    else:
        return ajaxResponse(already=True)

    return ajaxResponse()
