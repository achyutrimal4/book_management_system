from django import forms
from django.forms import ModelForm
from .models import Bill

class BillForm(ModelForm):
    sold_on = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Bill
        fields = ['customer', 'price', 'book', 'sold_on']