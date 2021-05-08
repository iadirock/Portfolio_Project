from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='image/')

    #to show title string instead of object in admin panel
    def __str__(self):
        return self.title

    #Creating function to show only 100 chars of the body
    def summary(self):
        return self.body[:100] + "..."

    #creating function to show preferred format of date
    def pub_date_new(self):
        return self.pub_date.strftime('%b %e %Y')