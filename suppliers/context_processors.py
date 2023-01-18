from .models import Supplier
from account import views as account_views

def extras (request):
    suppliers = Supplier.objects.all().order_by('-created')
    return {'suppliers':suppliers}