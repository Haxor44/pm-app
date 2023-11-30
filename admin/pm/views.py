from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.generics import GenericAPIView
from .paginator import PaginationHandlerMixin
# Create your views here.
from .models import Pmforms, USer
from .serializers import PmSerializer
from .producer import publish
import random


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'



             
class PmformsViewSet(viewsets.ViewSet,APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    serializer_class = PmSerializer

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator    
    
    def paginate_queryset(self, queryset):
        
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,self.request, view=self)    
    
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)   
     
    def get(self, request, format=None, *args, **kwargs):        
        instance = Pmforms.objects.all()
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)        
        else:
            serializer = self.serializer_class(instance, many=True)        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self,request):
        instance =Pmforms.objects.all()
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def search(self,request, format=None):
        record = Pmforms.objects.all()
        name = request.query_params.get('name')
        if name is not None:
            record = record.filter(name=name)
        serializer = PmSerializer(record,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        serializer = PmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("pmform_created",serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(Self, request, pk=None):
        pm = Pmforms.objects.get(id=pk)
        serializer = PmSerializer(pm)
        return Response(serializer.data)
    

    def update(Self, request, pk=None):
        pm = Pmforms.objects.get(id=pk)
        serializer = PmSerializer(instance=pm, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("pmform_updated",serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(Self, request, pk=None):
        pm = Pmforms.objects.get(id=pk)
        pm.delete()
        publish("pmform_deleted",pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class UserAPIView(APIView):
    def get(self,_):
        users = USer.objects.all()
        user = random.choice(users)
        return Response({
            "id":user.id
        })

    