from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Books
from django.contrib import messages

# Create your views here.

def books(request):
    form = BookForm()
    books = Books.objects.all().order_by('-created')
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book Saved')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Error!')
            form = BookForm(request.POST)
    
    context = {'form': form, 'books': books}
    return render(request, 'books/books.html', context)
