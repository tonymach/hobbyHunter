from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from transactions.models import Session, MerchantEndpointLink, SessionEndpoint
from search.models import merchantPages, Page
from misc.funcs import accTypeis as aT

from transactions.transSchemes import voodooDoctor as vD
# Create your views here.

@login_required(login_url='/merchant/login/')
def index(request):
    if aT(request,'M'):
        return render(request, 'merchant/index.html')
    else:
        return redirect ('/my/calendar/')

def register(request):
    return render(request, 'merchant/register/index.html')


def login(request):
    return render(request, 'merchant/login/index.html')

@login_required(login_url='/merchant/login/')
def settings(request):
    if aT(request,'M'):
        return render(request, 'merchant/settings/index.html')
    else:
        return redirect ('/my/settings/')


@login_required(login_url='/merchant/login/')
def pages(request):
    """
    ManagePage Context
    """
    merchant = request.user.email
    context = {}
    pages = []
    linkEndpoints = vD.getMerchantEndpointLink(merchant)
    sessions = []

    if linkEndpoints.endPoints != None:
        for each in linkEndpoints.endPoints:
            print(each)
            if SessionEndpoint.objects.filter(pk=each):
                temp = SessionEndpoint.objects.get(pk=each)
                sessions.append(temp)
                print(temp.datetime)

    if merchantPages.objects.filter(pk=request.user.email):
        temp = merchantPages.objects.get(pk=request.user.email)
    else:
        temp = None
    if temp != None:
        for i in temp.endPoints:
            pages.append(Page.objects.get(pk=i))



    context['pages'] = pages
    context['sessions'] = sessions

    return render(request, 'merchant/pages/index.html', context)





@login_required(login_url='/merchant/login/')
def startSession(request,sessionId, pageId):
    """
    session Scanning and all
    """
    context = {}
    if Session.objects.filter(pk=sessionId):
        session = Session.objets.get(pk=sessionId)
    if Page.objects.filter(pk=pageId):
        page = Page.objects.get(pk=pageId)
    context['page']  = page
    return render(request, 'merchant/transaction/index.html', context)
