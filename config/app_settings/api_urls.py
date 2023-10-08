from django.urls import path
from .api_views import *

app_name = 'app_settings'

urlpatterns = [
    path('get-channels/',GetChannels.as_view(),name='GetChannels'),
]