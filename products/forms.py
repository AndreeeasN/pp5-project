from django import forms
from .models import Product, ProductVariant, Category


class ProductForm(forms.ModelForm):
    """
    Forms for adding new products
    """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_friendly = [(c.id, c.get_friendly_name()) for c in categories]
        variants = ProductVariant.objects.all()
        variant_friendly = [(v.id, v.get_friendly_name()) for v in variants]

        multiSelectString = ' (Hold Ctrl to multi-select)'
        self.fields['category'].choices = category_friendly
        self.fields['product_variants'].choices = variant_friendly
        self.fields['product_variants'].label += multiSelectString
        self.fields['product_tags'].label += multiSelectString
