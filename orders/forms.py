from django import forms
from .models import Order
from account.models import MyUser

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderType']