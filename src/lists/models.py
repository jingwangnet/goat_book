from django.db import models
from django.urls import reverse


# Create your models here.
class List(models.Model):
    def get_absolute_url(self):
        return reverse("lists:view", args=[self.pk])


class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)
