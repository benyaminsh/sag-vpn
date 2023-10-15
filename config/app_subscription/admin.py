from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    fields = ('code', 'fullname', 'period_of_time','status')
    list_display = ['code','fullname','period_of_time','status']
    search_fields = ['code','fullname']


admin.site.register(Subscription, SubscriptionAdmin)
