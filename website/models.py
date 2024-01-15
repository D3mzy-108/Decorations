from django.db import models


class Design(models.Model):
    description = models.TextField()
    likes = models.IntegerField(default=0)
    price = models.FloatField(null=True)
    image = models.ImageField(upload_to='designs/', null=True)
    delivery_fee = models.FloatField(null=True, blank=True)
