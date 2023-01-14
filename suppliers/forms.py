from django.forms import ModelForm
from django import forms
from .models import Supplier

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'