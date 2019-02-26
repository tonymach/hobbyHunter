from django.shortcuts import render

from indexSuggestions.models import Choice

from hobbyHunter.master import master
workin = master.workin()


def add(request):

    print('ADDED FUNCTION')
    response_data = {}
    image = request.FILES['mainImage']
    skill = request.POST.get('skill')
    description = request.POST.get('description')
    try:
        IndexSuggestions.Internal.add(skill=skill, description=description, image=image)
        response_data['result']='success'
        workin
    except:
        response_data['result']='error'


def remove(request):
    pass





class IndexSuggestions(object):
    """
    Handles the choice boxes on the index and other places in the future
    """
    class Return:
        def new(self):
            temp = [for i in range(6) IndexSuggestions.Internal.display()]
            return temp



    class Internal:
        def add(self, skill, image, description):
            try:
                choice = Choice.objects.create(skill=skill,mainImage=image, description=description)
                choice.save()
                return True
            except:
                return False

        def remove(self, skill):
            choice = Choice.objects.get(skill=skill)
            try:
                choice.delete()
                return True
            except:
                return False

        def display(self):
            random_idx = randint(0, Choice.objects.count() - 1)
            choice = Choice.objects.all()[random_idx]
            return choice
