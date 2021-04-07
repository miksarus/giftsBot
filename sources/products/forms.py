from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'update_date',
            'name',
            'ozone_id'
        )
        widgets = {
            'update_date' : forms.DateTimeField,
            'name': forms.TextInput,
            'ozone_id': forms.TextInput,
        }