from django.shortcuts import render, redirect
from .forms import BillForm
from django.contrib import messages
from books.models import Books
from customers.models import Customer
from .models import Bill

# Create your views here.
def accounting(request):
    form = BillForm()
    bills= Bill.objects.all().order_by('-created')
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            # retrieve form data
            price = form.cleaned_data['price'] #Selling price
            book_name = form.cleaned_data['book']
            customer_name = form.cleaned_data['customer']
            sold_date = form.cleaned_data['sold_on']
            
            
            book = Books.objects.get(name=book_name)
            buying_cost = book.price
            profit_loss = price-buying_cost      
            newBill = Bill(profit_loss=profit_loss, price=price, book=book_name, customer=customer_name, sold_on=sold_date)  
            newBill.save()
            messages.success(request, 'Bill Created')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Error!')
            form = BillForm(request.POST)           
            
    context = {'form': form,'bills':bills}
    return render(request, 'account/account.html', context)


    