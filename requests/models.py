from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

#Category tracks broad skill-type categories (i.e. Python, Java, Tax, Excel, etc.)
class Category(models.Model):
    username = models.CharField(max_length=30, default="John")                                   #Tracks who created what category
    name = models.CharField(max_length=100, default = "A Category")
    timestamp = models.DateTimeField(default = timezone.now())                  #Timestamp of when category created
    def __unicode__(self):
        return self.category_name

#Requests is a request for help by a user
class Request(models.Model):
    created_by = models.CharField(max_length=30, default="John")                                                          #Username from contrib.auth
    name = models.CharField(max_length=100, default = "A Project")
    time_in_hours = models.DecimalField(max_digits=4,decimal_places=2)          #Time request will take in hours
    timestamp = models.DateTimeField(default = timezone.now())                                  #Timestamp of request
    category_name = models.ForeignKey(Category)                                 #Category of request from Category Class
    number_of_people = models.DecimalField(max_digits=2,decimal_places=0)       #Number of people requested
    def __unicode__(self):
        return self.name

# # #Available identifies whether a user is available or not
# class Available(models.Model):
#     username = models.CharField(max_length=30, default="John")                                                             #Username from contrib.auth
#     is_available = models.BooleanField(default=None)
#     def __unicode__(self):
#         return self.username, self.is_available
#
# # #RequestAccept identifies who is currently accepting what request
# class RequestAccept(models.Model):
#     username = models.CharField(max_length=30, default="John")                    #Username from contrib.auth
#     request_id = models.ForeignKey(Request)                                    #Request from request class
#     def __unicode__(self):
#         return self.username, self.request_id
