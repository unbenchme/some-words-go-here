from django import modelform_factory
from django import modelForm
from DjangoStack.models import Category, Request, Available

# #Create the form class
class CatergoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['Category Name']

#Creating a form to add an article
form = CategoryForm

#Model form factory function - for front end facing forms
CategoryForm = modelform_factory(Category, fields=("name", "username"))
RequestForm = modelform_factory(Request, fields=("name","time_in_hours", "category_name", "number_of_people","created_by"))
