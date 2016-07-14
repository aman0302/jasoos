from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from karamchand.models import Case
from karamchand.serializers import CaseSerializer
from karamchand.forms import CaseForm


# Create your views here.

@api_view(['GET'])
def list_cases(request):
    if request.method == 'GET':
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def view_case(request, id):
    try:
        case = Case.objects.get(id=id)
    except Case.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CaseSerializer(case)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_case(request):
    if request.method == 'GET':
        posts = Case.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'text': request.DATA.get('the_post'), 'author': request.user.pk}
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
