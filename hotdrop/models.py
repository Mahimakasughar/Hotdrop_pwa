from django.db import models

STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled"),
]

PAYMENT_CHOICES = [
    ("Cash on Delivery", "Cash on Delivery"),
    ("Card", "Card"),
]

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default="Cash on Delivery")

    date_ordered = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Order #{self.id} - {self.full_name}"

from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    password = models.CharField(max_length=100)  # plain text for now
    is_approved = models.BooleanField(default=False)

    def _str_(self):
        return self.name
    
class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=200)

    def _str_(self):
        return self.name

class Order(models.Model):
    # existing fields...
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="Pending")
    payment_method = models.CharField(max_length=50, default="COD")
    date_ordered = models.DateTimeField(auto_now_add=True)
    
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)

    def _str_(self):
        return f"Order #{self.id} - {self.full_name}"