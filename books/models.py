from django.db import models
import uuid

# Create your models here.
class Books(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)    
    name = models.CharField(max_length=250)
    purchase_date = models.DateField(verbose_name='Date of Purchase')
    isbn = models.CharField(max_length=250)
    price = models.FloatField(verbose_name='Price')    
    created = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    def __str__(self):
        return self.name