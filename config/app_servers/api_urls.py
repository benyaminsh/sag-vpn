from django.urls import path
from .api_views import *

app_name = 'app_server'

urlpatterns = [
    path('create-config/',CreateConfig.as_view(),name='CreateConfig'),
    path('get-config/<str:code>/',GetConfig.as_view(),name='GetConfig'),
]