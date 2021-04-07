from django import forms
from .models import Product
from .models import Category
from .models import Mark

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        price = forms.IntegerField(min_value=0)
        category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="(Nothing)")
        marks = forms.ModelMultipleChoiceField(queryset=Mark.objects.all())

        fields = (
            'name',
            'ozone_id',
            'price',
            'category',
            'marks'
        )
        widgets = {
            'name': forms.TextInput,
            'ozone_id': forms.TextInput
        }