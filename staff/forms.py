from django import forms
from account.models import MyUserOrdering
from orders.models import MyOrderOrdering

class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = MyUserOrdering
        fields = ['attributeChosen','OrderOfCustomers']

class OrdersOrderForm(forms.ModelForm):
    class Meta:
        model = MyOrderOrdering
        fields = ['attributeChosen','OrderOfOrders']