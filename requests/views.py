from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import newRequest

from .models import Category, Request, Available


# views go here

def activeRequests(request):
    #all active requests in list format, boring i know
    active_request_list = Request.objects.all()
    context = { 'active_request_list': active_request_list}
    return render(request, 'requests/index.html', context)

def allCategories(request):
    #all categories in list format
    all_categories_list = Category.objects.all()
    context = { 'all_categories_list': all_categories_list}
    return render(request, 'requests/categories.html', context)

def allAvailable(request):
    #all available people in list format
    all_available_list = Available.objects.all()
    context = { 'all_available_list': all_available_list}
    return render(request, 'requests/available.html', context)

def get_request(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = newRequest(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = newRequest()

    return render(request, 'newrequest.html', {'form': form})
