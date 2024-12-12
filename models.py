from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    banner = models.ImageField(default='default' ,blank=True, null=True, upload_to='static/image')
    class Meta:
        ordering = ['-created', '-updated']
    def __str__(self):
        return self.name
