from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .models import PmStaff, User
from .serializers import PmSerializer
import requests

class PmstaffViewSet(viewsets.ViewSet):
    def list(self, request):
        pm = PmStaff.objects.all()
        serializer = PmSerializer(pm, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        pm = PmStaff.objects.get(id=pk)
        serializer = PmSerializer(pm)
        return Response(serializer.data)

    def update(self, request,pk=None):
        pm = PmStaff.objects.get(id=pk)
        serializer = PmSerializer(instance=pm,data=serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None):
        pm = PmStaff.objects.get(id=pk)
        pm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def user(self, request):
        req = requests.get("http://localhost/api/user")
        return req.json()