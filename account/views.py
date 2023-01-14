from django.shortcuts import render

# Create your views here.
def accounting(request):
    return render(request, 'account/account.html')