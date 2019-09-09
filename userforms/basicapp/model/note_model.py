from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
# Create your models here.




class Note(models.Model):
    title = models.CharField(max_length = 256)
    content = models.CharField(max_length=1024,default=" ")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse("basicapp:user_dashboard")
    def __str__(self):
        return self.title
