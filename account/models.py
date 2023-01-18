from django.db import models
import uuid
from customers .models import Customer
from books .models import Books

# Create your models here.
class Bill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False) 
    customer = models.ForeignKey(Customer, null=True, blank=False, on_delete=models.SET_NULL)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    sold_on = models.DateField(null=True)
    profit_loss = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.customer.name