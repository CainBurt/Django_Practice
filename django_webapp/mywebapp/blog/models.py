from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #returns the path to go to after a new post is created
    def get_absolute_url(self):
        return reverse('postdetail-page', kwargs={'pk': self.pk})
