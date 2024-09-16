from django.db import models
from django.contrib.auth.models import User

class Freelancers(models.Model):
    title = models.CharField(max_length=50)
    bio = models.TextField()
    skill = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hour_rates = models.IntegerField()

    def __str__(self):
        return self.title

