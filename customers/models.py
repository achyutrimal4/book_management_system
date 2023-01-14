from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)    
    name = models.CharField(max_length=250)
    pan = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.name