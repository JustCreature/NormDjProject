from django.db import models

# Create your models here.
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse("courses:courses-detail", kwargs={"id": self.id})
