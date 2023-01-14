from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SupplierForm
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'suppliers/dashboard.html' )

def suppliers(request):
    form = SupplierForm()
    
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier added')
            return redirect(request.META['HTTP_REFERER'])
            # return HttpResponse(request.POST.items())
        else:
            form = SupplierForm(request.POST)
    context = {'form': form}
    return render(request, 'suppliers/suppliers.html', context)