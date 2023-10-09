from django.db import models

class Servers(models.Model):
    config = models.TextField(unique=True)
    channel = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.config

    class Meta:
        ordering = ['-id']