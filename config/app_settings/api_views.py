from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Channels
from .serializers import ChannelsSerializers


class GetChannels(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChannelsSerializers
    queryset = Channels.objects.all()

class CreateChannel(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChannelsSerializers
    queryset = Channels.objects.all()
