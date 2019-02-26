from django.shortcuts import render
from datetime import date

from misc.funcs import TryMe

from django.contrib.auth.decorators import login_required

from transactions.models import SessionEndpoint
from transactions.transSchemes import voodooDoctor as vD
from search.models import Page


@login_required(login_url='/')
def index(request):
    context = {}
    # context['calendar'] = calendar
    context['tryme'] = TryMe.grab()
    context['datetime'] = date.today().isoformat()
    tempPages =  vD.JsonIn(request.user.GetclassKeys())
    pages = []
    for key, page in tempPages.items():
        print(page['pageName'])
        listing = Page.objects.get(pk=page['pageName'])
        session = SessionEndpoint.objects.get(pk=key)

        print(listing.title)
        pages.append({
        'pageId': listing.pageId,
        'title': listing.title,
        'sessionId': key,
        'key': page['key'],
        'when': session.datetime
        })
        print(pages)

    context['pages'] = pages

    return render(request, 'user/index.html',context)

@login_required(login_url='/')
def settings(request):
    context = {}
    context['datetime'] = date.today().isoformat()
    return render(request, 'user/settings/index.html',context)
