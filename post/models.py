from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField(max_length = 1501)
    created_at = models.DateTimeField(default= timezone.now)
    image = models.ImageField(upload_to='post-ing/', height_field=None, width_field=None, max_length=100)
    
    
    
    

    def __str__(self):
        return self.title

  