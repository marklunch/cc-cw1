from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from datetime import datetime, timedelta

# Create your models here.
class Messages(models.Model):
    CATEGORY_CHOICES = (
        ('politics', 'Politics'),
        ('health', 'Health'),
        ('sport', 'Sport'),
        ('technology', 'Technology'),
    )
    poster = models.ForeignKey(settings.AUTH_USER_MODEL,\
        on_delete=models.CASCADE,\
        related_name='posts', default=1)    #user.posts.all() returns all messages a user has created
    title = models.CharField(max_length=100)
    body = models.TextField("Message Body")
    postDate = models.DateTimeField("Date Posted", default=timezone.now)
    expirySeconds = models.IntegerField("Duration in seconds", default=0)
    expiryTime = models.DateTimeField("Expiry time and date", default=timezone.now)
    active = models.BooleanField("Message is active?", default=True)
    category = models.CharField(max_length=20, \
        choices=CATEGORY_CHOICES)    #No need for a default value

    class Meta:
        ordering = ('-postDate',)

    def __str__(self):
        return self.title

#Override the save method as suggested by StackOverflow user Vyacheslav: 
# https://stackoverflow.com/questions/56202798/how-to-convert-a-models-integerfield-to-an-integer
#Calculate the expiry time by adding the expiry Seconds to the creation date.  Can be adjusted on each save also.
#Then set active status according to the two timestamps.

    def save(self, *args, **kwargs):
        self.expiryTime = self.postDate + timedelta(seconds=self.expirySeconds)
        if self.expiryTime<=self.postDate:
            self.active = False
        else:
            self.active = True
        super(Messages, self).save(*args, **kwargs)


class Reactions(models.Model):
    REACTION_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    reactor = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reactions')
    message = models.ForeignKey(Messages,on_delete=models.CASCADE, related_name='reactions')
    reactDate = models.DateTimeField("Reaction Date and Time", default=timezone.now)
    reactType = models.CharField(max_length=8,\
        choices=REACTION_CHOICES)

    class Meta:
        ordering = ('-reactDate',)

    def __str__(self):
        return self.message.title

    def showPoster(self):
        return self.message.poster

    def save(self, *args, **kwargs):
        if self.message.active == False:
            return
        if(self.reactor==self.message.poster): #If True, the op is trying to react to their own post.
            return  #Change to exception before testing
        super(Reactions, self).save(*args, **kwargs)

class Comments(models.Model):
    message = models.ForeignKey(Messages,on_delete=models.CASCADE, related_name='comments')
    commentor = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField("Comment")
    dateCommented = models.DateTimeField("Date and Time", default=timezone.now)

    def showTitle(self):
        return self.message.title

    def save(self, *args, **kwargs):
        if self.message.active == False:
            return
        super(Comments, self).save(*args, **kwargs)

