from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    file = models.FileField(upload_to='songs')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
    def delete(self, *args, **kwargs):
        # Remove the file when the record is deleted
        if self.file:
            # Get the file path
            file_path = self.file.path
            # Delete the file from the file system
            if os.path.exists(file_path):
                os.remove(file_path)
        super().delete(*args, **kwargs)

