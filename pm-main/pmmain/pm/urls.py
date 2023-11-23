from django.contrib import admin
from django.urls import path
from .views import PmstaffViewSet

urlpatterns = [
    path('pm', PmstaffViewSet.as_view({
        'get':'list',
        'post':'create'
    })),

    path('pm/<str:pk>', PmstaffViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),

    path('user', PmstaffViewSet.as_view({
        'get':'user',
    })),
    
]