from rest_framework import generics,response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import HttpResponse
from .models import *
from .serializers import ServersSerializers
from app_subscription.models import Subscription
from datetime import datetime
from random import choice
from django.utils import timezone
from app_settings.models import Ads


def check_date(date):
    now = datetime.now().date()
    if date < now:
        return True
    else:
        return False



class CreateConfig(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServersSerializers
    queryset = Servers.objects.all()


def get_config():
    emoji = [
        "👽",
        "🐶",
        "🦮",
        "🐕‍🦺",
        "🐩",
        "🪐",
        "💫",
        "☄️",
        "🌕",
        "🚀",
    ]
    servers = ""
    count = 0
    for server in filter(lambda x: "ss://" not in  x.config ,Servers.objects.all()):
        try:
            ads = Ads.objects.last()
            if ads is None:
                ads = "default"

            else:
                ads = ads.text

            if ads == 'default':
                emoji_select = choice(emoji)
                result = str(server.config).split('#')[0] + f"# Dog Vpn  {emoji_select}"
                if len(server.config) != 0:
                    servers += f"{result}\n"
                    emoji.remove(emoji_select)


            else:
                result = str(server).split('#')[0] + f"#{ads}"
                servers += f"{result}\n"


        except:
            servers += f"\n{server}"


        count+= 1
        if count == 10:
            break


    return servers


class GetConfig(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        code = self.kwargs['code']
        subscription = Subscription.objects.filter(code=code).first()
        if subscription is not None:
            if check_date(subscription.expire_date):
                if subscription.status:
                    subscription.status = False
                    subscription.save()
                return HttpResponse('Your subscription has expired', content_type='text/plain')
            else:
                thirty_days_ago = timezone.now() - timezone.timedelta(days=2)
                queryset = Servers.objects.filter(date=thirty_days_ago).delete()
                return HttpResponse(get_config(), content_type='text/plain')
        else:
            return HttpResponse('You do not have access', content_type='text/plain')


class GetStatusServers(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServersSerializers
    queryset = Servers.objects.all()

    def get(self, request, *args, **kwargs):
        date_now = datetime.now()
        servers = Servers.objects.filter(date__year=date_now.year,date__month=date_now.month,date__day=date_now.day).count()
        return response.Response({'count': servers})



