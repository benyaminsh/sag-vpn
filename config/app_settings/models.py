from django.db import models


class Channels(models.Model):
    username = models.CharField(max_length=255,unique=True,verbose_name="Username Example : @vop_org")

    def __str__(self):
        return self.username


class Ads(models.Model):
    text = models.TextField(default='default')

    def __str__(self):
        return self.text