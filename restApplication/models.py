from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
<<<<<<< HEAD
    
=======

>>>>>>> f9707feb15964d459c386930b10b979e69e1b492
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
