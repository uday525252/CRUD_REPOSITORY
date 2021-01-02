from django.db import models
from django.urls import reverse

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=30)
    hero=models.CharField(max_length=20)
    heroine=models.CharField(max_length=30)
    releasedate=models.DateField()


    def get_absolute_url(request):
        return reverse("detail")
