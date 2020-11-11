from django import forms
from shop.models import Category, Product, MyProductOrdering, MyCategoryOrdering
from account.models import MyUserOrdering
from coupons.models import Coupon, MyCouponOrdering

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'image','description', 'price', 'available', 'category']

class CouponCreateForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['code', 'valid_from', 'valid_to', 'discount', 'active']

class ProductsOrderForm(forms.ModelForm):
    class Meta:
        model = MyProductOrdering
        fields = ['attributeChosen','OrderOfProducts']

class CategoryOrderForm(forms.ModelForm):
    class Meta:
        model = MyCategoryOrdering
        fields = ['attributeChosen','OrderOfCategories']

class EmployeesOrderForm(forms.ModelForm):
    class Meta:
        model = MyUserOrdering
        fields = ['attributeChosen','OrderOfCustomers']

class CouponOrderForm(forms.ModelForm):
    class Meta:
        model = MyCouponOrdering
        fields = ['attributeChosen','OrderOfCoupons']