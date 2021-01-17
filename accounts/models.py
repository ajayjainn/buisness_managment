from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    amountPending = models.IntegerField(default=0)
    phoneNo = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, related_name='transaction', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    tea = models.DecimalField(default=0, decimal_places=1, max_digits=3)
    amount = models.IntegerField(default=0)
    closingBalance = models.IntegerField()
    remarks = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.customer.name +' '+ str(self.date)
    