from random import randint
from misc.models import tryMe
import json
from django.http.response import HttpResponse
class TryMe(object):
    """
    Handles TryMe's
    """
    def grab():
        """
        Gets a tryMe
        """
        random_idx = randint(0, tryMe.objects.count() - 1)
        trymeObject = tryMe.objects.all()[random_idx]
        return trymeObject.thing

    def put(string):
        """
        Puts a TryMe
        """
        try:
            temp = tryMe.objects.create()
            temp.thing = string
            temp.save()
            return True
        except:
            return False

    def delete(string):
        """
        Delete's TryMe"
        """
        temp = tryMe.objects.get(pk=string).delete()
        return True

def accTypeis(request,string):
    """
    (request, string) => Bool
    if user is accType, return True
    """
    if request.user.accType == string:
        return True
    else:
        return False

def ajaxResponse(error=False, already=False):
    """(bool, bool) => HttpResponse
    Input error and already and returns bool
    No extra ifs required
    """
    response={}
    if not error:
        if not already:
            respondKey = 'success'
        else:
            respondKey = 'already'
    else:
        respondKey = 'error'
    response['result'] = respondKey
    return HttpResponse(
        json.dumps(response),
    content_type="application/json"
        )
