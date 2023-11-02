from django import forms 
from .models import Product

class productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "decription", "category", "rating", "image"]