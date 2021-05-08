from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='image/')
    summary=models.CharField(max_length=300)

    #to show title string instead of object in admin panel
    def __str__(self):
        return self.title