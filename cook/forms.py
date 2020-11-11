from django import forms
from orders.models import MyOrderOrdering, MyOrderItemOrdering

class OrderItemsOrderForm(forms.ModelForm):
    class Meta:
        model = MyOrderItemOrdering
        fields = ['attributeChosen','OrderOfOrders']