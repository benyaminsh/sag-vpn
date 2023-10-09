from django.urls import path
from .api_views import *

app_name = 'app_settings'

urlpatterns = [
    path('get-ads/',GetAds.as_view(),name='GetAds'),
    path('get-channels/',GetChannels.as_view(),name='GetChannels'),
    path('create-channels/',CreateChannel.as_view(),name='CreateChannel'),
]