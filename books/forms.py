from django.forms import ModelForm
from django import forms
from .models import Books

class BookForm(ModelForm):
    purchase_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Books
        fields = '__all__'