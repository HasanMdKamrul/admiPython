from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TestApi
# Create your views here.
from .serializers import TestApiSerializers

# https://blog.devgenius.io/genericapiview-and-mixins-in-drf-28ac6192bd2f

# ** Exploring Api views

class ApiTestView(APIView):
    
    def get(self,*args,**kwargs):
        my_data = TestApi.objects.filter(id=13)
        print(type(my_data.values()))
        # print("my", my_data.pk)
        # print("my",my_data)
        # print("count",my_data.values_list().annotate())
        # for item in my_data.values():
        #     print(item)
        # returned = [item for item in my_data.values_list()[0]]
        # print("returned",returned)
        return Response({
            "data" :(my_data.values())
        })

    def post(self,request,*args,**kwargs):
        payload = TestApi.objects.create(
            name = request.data["name"],
            description = request.data["description"],
            phone_no = request.data["phone_no"],
            is_alive = request.data["is_alive"],
            amount = request.data["amount"],
        )
        
        print("payload",payload)
        print("modelto dict",model_to_dict(payload))
        
        return JsonResponse({
            "data" : model_to_dict(payload)
        })
class ListApiCreateView(generics.ListCreateAPIView):
    serializer_class = TestApiSerializers
    queryset = TestApi.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        # print(model_to_dict(queryset))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data) 

    def create(self, request, *args, **kwargs):
        data = request.data
        if data["is_alive"]:
            print("Yess")
        # print(data["phone_no"])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CurrentApiView(generics.ListAPIView):
    serializer_class = TestApiSerializers
    queryset = TestApi.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        created_object = TestApi.objects.create(phone_no = "019232")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    # def get(self, request, *args, **kwargs):
        