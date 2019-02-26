from collections import Counter
import re
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
w = HttpResponse("Works!")

from search.QueryFuncs import Query, Parse
from search.models import Page, Index, Keyword

from transactions.transSchemes import voodooDoctor as vD
from misc.funcs import TryMe
# Create your views here.

def launch(request):
    return render(request,'search/launch.html')



def index(request):
    # This is the final array with all of the cleaned pageIds in revelancy order
    pages = []
    # This is the search/query from Get
    search = request.GET.get('q')

    # If there is a search var

    if search:

        # proccess the query and returns ids, deals with either the main index or keyword one,
        #  and will deal with updating index after getting keyword id's
        results = Query.proccess(query=search)

        # Iterate thorugh the result Ids
        for i in results:

            # if page id exists append tempPage object to pages list
            if  Page.objects.filter(pk=i).exists():
                tempPage = Page.objects.get(pk=i)
                pages.append(tempPage)
            # Otherwise run the Admin.remove function and remove model from all
            #  Though will take care of it later
            else:
                print('broken')
                # remove broken pageId & not append anything
                # page = Page.objects.create(pageId=i,stars=0,lat=1.1,lon=1.2, averageCost=450)
                # page.save()
        if pages == []:
            pages = None
        context = {
        'query': search,
        'pages': pages,
        'stars': range(0,5),
        'tryme': TryMe.grab()
        }

        return render(request,'search/index.html',context)

    else:
        return render(request,'search/index.html')


# Empty? No url; maybe later!?
def search(request):
    return w

def listing(request,id):

    context = {}

    schedule = vD.getSchedule(id)
    context['schedule'] = schedule
    for i in schedule:
        print(i.datetime)
    if request.GET.get('intent'):
        intent  = request.GET.get('intent')

    # Check if page actually exist
    if  Page.objects.filter(pk=id).exists():
        page = Page.objects.get(pk=id)
    else:
        page = None
    # The actual page
    context['listing'] = page

    # Dev star bullshit
    context['stars'] = range(0,page.stars)

    # Date to make it faster to display
    context['datetime'] = date.today().isoformat()

    # The return
    return render(request,'search/listing/index.html',context)


def fillCalendar(request):
    """
    Returns a json object with a date -> endpoint
    """
