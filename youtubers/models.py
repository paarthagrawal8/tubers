from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Youtuber(models.Model):
    crew_choices =(
        ('small' ,'small'),
        ('medium','medium'),
        ('large','large'),
    )

    camera_choices = (
        ('sony','sony'),
        ('nikon','nikon'),
        ('fuji','fuji'),
        ('cannon','cannon'),
    )

    category_choices = (
        ('gaming','gaming'),
        ('coding','coding'),
        ('teaching','teaching'),
        ('buisiness','buisiness'),
    )

    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to = 'media/ytubers/%Y')
    video_url = models.CharField(max_length=200)
    description = RichTextField()
    city = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices = crew_choices ,max_length=200)
    camera_type = models.CharField(choices = camera_choices , max_length=200) 
    subs_count = models.CharField(max_length=200) 
    category = models.CharField(choices = category_choices , max_length=200) 
    is_featured = models.BooleanField(max_length=200) 
    created_date = models.DateTimeField(default = datetime.now , blank=True ) 

    
       
    