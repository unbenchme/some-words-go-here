from django.forms.models import modelform_factory
from django.forms import ModelForm
from django import forms
from .models import Category, Request

# #Create the form class
class CatergoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class newRequest(ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'time_in_hours', 'category_name']

#Model form factory function - for front end facing forms
CategoryForm = modelform_factory(Category, fields=("name", "username"))
newRequest = modelform_factory(Request, fields=("name","time_in_hours", "category_name", "number_of_people","created_by"))
