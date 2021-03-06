from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

class Menu(models.Model):
    name = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image_menu', null=True, blank=True)

class image_promotion(models.Model):
    image1 = models.ImageField(upload_to='image_promotion', null=True, blank=True)
    name1 = models.CharField(max_length=20)
    price1 = models.DecimalField(max_digits=8, decimal_places=2)
    image2 = models.ImageField(upload_to='image_promotion', null=True, blank=True)
    name2 = models.CharField(max_length=20)
    price2 = models.DecimalField(max_digits=8, decimal_places=2) 
    image3 = models.ImageField(upload_to='image_promotion', null=True, blank=True)
    name3 = models.CharField(max_length=20)
    price3 = models.DecimalField(max_digits=8, decimal_places=2) 
    image4 = models.ImageField(upload_to='image_promotion', null=True, blank=True)
    name4 = models.CharField(max_length=20)
    price4 = models.DecimalField(max_digits=8, decimal_places=2)

class image_pagemenu(models.Model):
    image = models.ImageField(upload_to='image_pagemanu', null=True, blank=True)

class image_main(models.Model):
    image = models.ImageField(upload_to='image_main', null=True, blank=True)
    description = models.TextField(max_length=100)

class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def sub_total(item):
        return item.product.price * item.quantity    
    def __str__(self):
        return self.product.name

class Table(models.Model):
    status = models.BooleanField(default=True)

class Order(models.Model):
    table = models.IntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    email = models.EmailField(max_length=250, blank=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)

    def subtotal(self) :
        return self.quantity*self.price

