from django.db import models
from django.utils import timezone
import uuid

def generate_unique_code():
    code = str(uuid.uuid4())[:20]
    return code


class Subscription(models.Model):
    code = models.CharField(max_length=255,unique=True,default=generate_unique_code)
    fullname = models.CharField(max_length=200)
    expire_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    period_of_time = models.IntegerField(default=1,verbose_name='day')

    def save(self, *args, **kwargs):
        if self.period_of_time:
            sub_day = timezone.now() + timezone.timedelta(days=self.period_of_time)
            self.expire_date = sub_day

        super().save(*args, **kwargs)


    def __str__(self):
        return self.fullname


