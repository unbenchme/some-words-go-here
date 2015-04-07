from django.shortcuts import render
from django.http import HttpResponse

from .models import Category
from .models import Request


# views go here

def activeRequests(request):
    #all active requests in list format, boring i know
    active_request_list = Request.objects.all()
    context = { 'active_request_list': active_request_list}
    return render(request, 'requests/index.html', context)
