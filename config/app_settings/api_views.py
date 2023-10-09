from rest_framework import generics,response
from rest_framework.permissions import IsAuthenticated
from .models import Channels,Ads
from .serializers import ChannelsSerializers,AdsSerializers


class GetAds(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AdsSerializers
    queryset = Ads.objects.all()

    def get(self, request, *args, **kwargs):
        ads = Ads.objects.last()
        if ads is None:
            ads = 'default'
            return response.Response({'text': ads})
        else:
            return response.Response({'text': ads.text})

class GetChannels(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChannelsSerializers
    queryset = Channels.objects.all()

class CreateChannel(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChannelsSerializers
    queryset = Channels.objects.all()
