from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.TextField(null=True,blank=True)
    Mobile=models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.user.username