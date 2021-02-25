from django.db import models
import datetime

# Create your models here.
class Work(models.Model):
    
    images = models.ImageField(upload_to = 'works/static/img/')
    titlle = models.CharField(max_length=100)
    summary = models.TextField(max_length=200)
    details = models.TextField()
    

    def __str__(self):
        return self.titlle
class Courses(models.Model):
    images = models.ImageField(upload_to = 'works/static/img/')
    titlle = models.CharField(max_length=100)
    details = models.TextField()

    # def __str__(self):
    #     return self.titlle
           


    




    

