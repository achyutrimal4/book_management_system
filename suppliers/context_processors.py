from .models import Supplier

def extras (request):
    suppliers = Supplier.objects.all().order_by('-created')
    return {'suppliers':suppliers}