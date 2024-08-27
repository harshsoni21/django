from django.db import models
from django.contrib.auth.models import User

# Creating first tweet category
class TweetType(models.Model):
    CATEGORY_CHOICES = [
        ('ENT', 'Entertainment'),
        ('SPT' , 'Sports'),
        ('NEW' , 'News'),
        ('TECH' , 'Technology'),
        ('OTH' , 'Other')
    ]
    category = models.CharField(
        max_length=4,
        choices=CATEGORY_CHOICES,
        default='OTH',
    )
        
    def __str__(self):
        return f"{self.get_category_display()}"
    
# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    category = models.ForeignKey(TweetType, on_delete=models.CASCADE,default=5)
    text = models.TextField(max_length = "240")
    photo = models.ImageField(upload_to = "photos/" , blank=True , null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
     
    def __str__(self):
        return f'{self.user.username} {self.text[:10]}'
    

class TweetInfo(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    tweetId = models.ForeignKey(Tweet,on_delete=models.CASCADE)
    tweetTags = models.CharField(max_length=80)
    tweetTagsSplitForm = models.JSONField(default=list)
    tweetInfo = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'user is sending that info {self.tweetInfo[:15]}'
