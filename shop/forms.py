from django import forms
from .models import MyProductSearch

class ProductSearchForm(forms.ModelForm):
    class Meta:
        model = MyProductSearch
        fields = ['attributeChosen','searchCriteria']