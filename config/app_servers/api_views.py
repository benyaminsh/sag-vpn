from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import HttpResponse
from .models import Servers
from .serializers import ServersSerializers
from app_subscription.models import Subscription
from datetime import datetime



def check_date(input_date):
    current_date = datetime.now().date()
    if input_date < current_date:
        return True
    else:
        return False


class CreateConfig(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServersSerializers
    queryset = Servers.objects.all()


class GetConfig(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        code = self.kwargs['code']
        subscription = Subscription.objects.filter(code=code).first()
        if subscription is not None:
            if check_date(subscription.expire_date):
                return HttpResponse('اشتراک شما به پایان رسیده است', content_type='text/plain')
            else:
                servers = ""
                for server in Servers.objects.all()[:6]:
                    servers += f"\n{server}"
                return HttpResponse(servers, content_type='text/plain')

        else:
            return HttpResponse('خطا', content_type='text/plain')
