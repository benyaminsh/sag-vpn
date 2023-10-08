from rest_framework import serializers
from .models import Channels

class ChannelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = "__all__"