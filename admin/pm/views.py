from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .models import Pmforms, USer
from .serializers import PmSerializer
from .producer import publish
import random

class PmformsViewSet(viewsets.ViewSet):
    def list(self,request):
        pm = Pmforms.objects.all()
        serializer = PmSerializer(pm, many=True)
        return Response(serializer.data)

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

    