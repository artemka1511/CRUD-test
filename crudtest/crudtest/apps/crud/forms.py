from .models import Products
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["title", "price", "description", "url"]
        widgets = {'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
        }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену ( руб )'
        }),
            'url': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на покупку'
        }),
    }