from django.db import models

class Subscription(models.Model):
    code = models.CharField(max_length=255,unique=True)
    fullname = models.CharField(max_length=200)
    expire_date = models.DateField(auto_created=True)

    def __str__(self):
        return self.fullname