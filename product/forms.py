from django import forms
from product.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'owner', 'description', 'condition', 'category', 'brand', 'price', 'image',)

class AdProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'condition', 'category', 'brand', 'price', 'image')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'image',)

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('brand_name',)

