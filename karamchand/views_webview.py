from django.http import JsonResponse
from django.shortcuts import render
from .forms import CaseForm

from karamchand.logic.clients.FacebookClient import FacebookClient
from karamchand.logic.chauffer.MealBuilder import MealBuilder
from karamchand.logic.config.DataSourceEnum import DataSourceEnum
from karamchand.logic.config.EntityInfoEnum import EntityInfoEnum


# Create your views here.

def case_create(request):
    # resp = FacebookClient.get_facebook_data("reliance")
    entity_info = {}
    entity_info[EntityInfoEnum.entity.name] = 'midtown comics'
    sources = []
    sources.append(DataSourceEnum.Facebook.name)
    sources.append(DataSourceEnum.Twitter.name)
    builder = MealBuilder(entity_info, sources)
    resp = builder.build_meal()
    return JsonResponse(resp)

def live_view(request):

    if request.method=="GET":
        form = CaseForm()
        return render(request, 'live_view.html',{'form':form})

    '''
    if request.method=='GET':
        return render(request, 'live_view_independent.html')
    '''

    if request.method=="POST":

        entity_info = {}

        for key, value in request.POST.items():
            entity_info[key]=value

        sources=[]

        for source in DataSourceEnum:
            if("on" == request.POST.get(source.name)):
                sources.append(source.name)

        builder = MealBuilder(entity_info, sources)
        resp = builder.build_meal()
        '''

        return render(request,'test_view.html');
        '''

    print ("1")
    return render(request,'test_view.html')


    '''

    '''