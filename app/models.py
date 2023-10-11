from django.db import models


# Create your models here.
class Log(models.Model):
    body = models.TextField()
    ipaddress = models.IPAddressField()
    result = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
