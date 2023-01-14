from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def customers_view(request):
    form = CustomerForm()
    customers = Customer.objects.all().order_by('-created')
    
    # data submission
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer added')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Error')
            form = CustomerForm(request.POST)

    context={'form':form, 'customers':customers}
    return render (request, 'customers/customers.html', context)