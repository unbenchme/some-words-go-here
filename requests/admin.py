from django.contrib import admin
from requests.models import Request, Category, Available, RequestAccept

#adding comments
# Register your models here.
admin.site.register(Request)
admin.site.register(Category)
admin.site.register(Available)
admin.site.register(RequestAccept)
