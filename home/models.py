from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    generated_order_id = models.CharField(max_length=50, default='000000')
    name = models.CharField(max_length=50, default='none')
    email = models.CharField(max_length=200, default='none')
    phone = models.CharField(max_length=15, default='none')
    for_class = models.CharField(max_length=10, default='none')
    paid = models.CharField(max_length=50, default='none')

    def __str__(self):
        return self.name
    