from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.activeRequests, name='activeRequests'),
    url(r'^categories/', views.activeRequests, name='allCategories'),
    url(r'^available/', views.allAvailable, name='allAvailable'),
    url(r'^newrequest/', views.get_request, name='get_request'),
]
