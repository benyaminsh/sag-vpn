from rest_framework import serializers
from .models import Channels,Ads

class ChannelsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = "__all__"


class AdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"