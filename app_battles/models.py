from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Battle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    my_platoons = models.TextField()
    opponent_platoons = models.TextField()
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
