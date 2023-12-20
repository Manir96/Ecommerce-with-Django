from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DIVISION_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Khulna','Khulna'),
    ('Barishal','Barishal'),
    ('Chattogram','Chattogram'),
    ('Mymenshing','Mymenshing'),
    ('Sylhet','Sylhet'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=50)
    villorroad = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    

    def __str__(self):
        return str(self.id)
    


CATEGORY_CHOICES = (
    ('LG', 'LEHENGA'),
    ('JL', 'JEWELLERY'),
    ('GP', 'GENTS PANT'),
    ('BK', 'BORKA'),
    ('EL', 'ELETRONICS'),
    ('SH', 'SHOES'),
    ('CL', 'CLOTHING'),
    ('SA', 'SAREE'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price



STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Pending')
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

