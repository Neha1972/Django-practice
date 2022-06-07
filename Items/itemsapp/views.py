from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import  api_view
from itemsapp.models import ItemModel
from .serializers import ItemSerializer
# Create your views here.

@api_view
def ItemsView(request):
 
    if request.method == 'GET':
        items = ItemsModel.objects.all()
        serializer = ItemSerializer(items, many =True)
        return JsonResponse(serializer.data, safe =False)
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =ItemSerializer(data = data)
 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)


@api_view
def ItemView(request,nm):
    try: 
        item = ItemsModel.objects.get(id = nm)
    except ItemsModel.DoesNotExist:
        raise Http404('Not found')
 
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)
 
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item,data =data)
 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)
 
    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status =204)