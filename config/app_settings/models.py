from django.db import models


class Channels(models.Model):
    username = models.CharField(max_length=255,verbose_name="Username Example : @vop_org")

    def __str__(self):
        return self.username