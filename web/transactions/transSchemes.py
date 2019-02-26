from transactions.encryptSchemes import livingDead as lD
from transactions.models import Session, SessionEndpoint, Schedule, MerchantEndpointLink
# from transactions.transSchemes import voodooDoctor as vD
from django.contrib.auth import get_user_model
User = get_user_model()

import json, pickle
from random import randint
from datetime import  date
from dateutil.relativedelta import relativedelta

from misc.funcs import ajaxResponse
import base64

class voodooDoctor(object):
    """
This handles absolutely all of the transactional process
So, voodooDoctor.book(banana, bleep)
    """

    def JsonIn(string):
        """
        json in data out
        """
        if string != '':
            b = json.loads(string)
        else:
            b = {}

        return b

    def JsonOut(data):
        """
        json in data out
        """
        b = json.dumps(data)
        return b


    def createId():
        """() -> string
        gens sessionId
        """
        return randint(10**5,10**6)




    # Create a session
    def createSession(merchant, session):
        """
        (string, string) => boolean
        | INTERNAL |
        """
        keys = lD.Frankenstein.findBrains()

        if Session.objects.filter(pk=session):
            sessionObject = Session.objects.get(pk=session)
        else:
            # Add support for custom date & time fields, for now testing
            sessionObject = Session.objects.create(id='%s_%s'%(merchant,session))

        try:
            sessionObject.save()
            voodooDoctor.addToMerchantEndpointLink(merchant)
            return True
        except:
            return False


    def getMerchantEndpointLink(merchant):
        """(merchant)-> linkObject
        """
        if not MerchantEndpointLink.objects.filter(pk=merchant):
            voodooDoctor.createMerchantEndpointLink(merchant)
        link = MerchantEndpointLink.objects.get(pk=merchant)
        return link


    def addToMerchantEndpointLink(merchant,sessionId):
        """(merchant, sessionId) -> bool
        Adds to link
        """
        try:
            if MerchantEndpointLink.objects.filter(pk=merchant):
                link = MerchantEndpointLink.objects.get(pk=merchant)
            if link.endPoints == None:
                link.endPoints = []
            link.endPoints.append(sessionId)
            link.save()
            return True
        except:
            return False

    def createMerchantEndpointLink(merchant):
        """(merchant) -> bool
        Creates Link
        """
        if not MerchantEndpointLink.objects.filter(pk=merchant):
            link = MerchantEndpointLink.objects.create(pk=merchant)
            link.save()
        return True

# ********************************************************************
# GRAB FOR PAGE
# ********************************************************************



    def grabSchedule(page):
        """(pageId) -> (queryset||None)
        [ INTERNAL   ]
        Returns queryset
        """

        sixMonths = date.today() + relativedelta(months=+6)
        try:
            schedule = Schedule.objects.filter(pageId = page, date__range=[date.today(), sixMonths])
        except:
            return None
        return schedule


    def grabSessions(schedule):
        """(scheduleObject) => context['date'] => obj
        [ INTERNAL   ]
        """
        context = []
        for endpoint in schedule:
            if endpoint.sessions != None:
                for each in endpoint.sessions:
                    if SessionEndpoint.objects.filter(pk=each):
                        temp = SessionEndpoint.objects.get(pk=each)
                        context.append(temp)
        return context


    def getSchedule(pageId):
        """(pageId) => pageScheduleObject
        |EXTERNAL  |
        """
        largeObject = voodooDoctor.grabSessions(voodooDoctor.grabSchedule(pageId))
        return largeObject


# ********************************************************************
# END OF GRAB FOR PAGE
# ********************************************************************


# ********************************************************************
# CREATE PAGE SCHEDULE, ENDPOINT, AND SESSION
# ********************************************************************


    def createPageSchedule(merchant,date,pageId,sessionId,spots):
        """(merchant,date,pageId,session,spots) => HttpResponse
        datetime,
        pageId,
        spots

        |EXTERNAL|
        """


        # Test fields
        #-----------------------
        # pageId = '68929840031'
        # merchant = 'A'
        # date = datetime.now()

        error = False
        already = False

        if not Schedule.objects.filter(pageId= pageId, date__exact=date):

            pageSchedule = Schedule.objects.create(pageId= pageId, date = date)

            if pageSchedule.sessions == None:
                pageSchedule.sessions = []

            pageSchedule.sessions.append(sessionId)


            # Create endPoint
            if voodooDoctor.createEndPoint(spots, date, sessionId, pageId):
                try:
                    pageSchedule.save()
                    voodooDoctor.addToMerchantEndpointLink(merchant,sessionId)
                except:
                    error = True

            else:
                error = True
        else:
            already = True
        return ajaxResponse(error, already)




    def createEndPoint(spots,dateTime,sessionId, pageId):
        """(maxInt, datetime, sessionId) => HttpResponse
        Create Endpoint
        |INTERNAL |
        """

        error = False
        already = False

        if not SessionEndpoint.objects.filter(pk=sessionId):
            endPoint = SessionEndpoint.objects.create(id = sessionId, spots=spots, datetime = dateTime, pageId=pageId)
            try:
                endPoint.save()
            except:
                error = True
        else:
            already = True

        if not error and not already:
            return True
        else:
            return False

# ********************************************************************
# ENDOF CREATE PAGE SCHEDULE, ENDPOINT, AND SESSION
# ********************************************************************





# ********************************************************************
# TRANSACTIONAL BOOKING AND VERIFY TRANSACTIONS
# ********************************************************************




    # User books a session
    def book(user, merchant, session):
        """
        (string, string ,string ) => boolean
        Will book session by using session id
        """

        authString = lD.Zombie.destroy(user)
        payload = authString['encryptedString']
        key = authString['key']

        payload = str(base64.b64encode(payload))
        key = str(base64.b64encode(key))
        # Adding key to user

        endpoint = SessionEndpoint.objects.get(pk=session)

        # JSON IN,
        # JSON OUT
        # MUST BE DONE TOMORROW
        if User.objects.filter(email=user):
            userObject = User.objects.get(email=user)
            temp = voodooDoctor.JsonIn(userObject.user_classKeys)

            temp[session] = {
            'key': key,
            'pageName': endpoint.pageId
            }
            print(temp)
            userObject.user_classKeys = voodooDoctor.JsonOut(temp)
            userObject.save()
        else:
            return False

        # Remove from spots
        endpoint.spots -= 1
        endpoint.save()

        # Adding authString to session
        if Session.objects.filter(pk=session):
            sessionObject  = Session.objects.get(pk=session)
            if sessionObject.users:
                temp = sessionObject.users
                temp = voodooDoctor.JsonIn(temp)
            else:
                temp = {}
            temp[user] = payload
            sessionObject.users = voodooDoctor.JsonOut(temp)
            sessionObject.save()

        else:
            return False

        try:
            sessionObject.save()
            return True

        except:
            return False

    # Verify session validity
    def verify():

        pass


# ********************************************************************
# TRANSACTIONAL BOOKING AND VERIFY TRANSACTIONS
# ********************************************************************
