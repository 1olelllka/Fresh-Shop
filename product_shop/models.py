from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    sale = models.BooleanField(default=False)
    old_price = models.PositiveSmallIntegerField(default=None, blank=True, null=True)
    price = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='photo/%d')
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Category(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='category/%d', blank=True, null=True, default=None)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug':self.slug})
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class GetInTouch(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Get In Touch'
        verbose_name_plural = 'Get In Touch'

# class Checkout(models.Model):
#     first_name = models.CharField(max_length=120)
#     last_name = models.CharField(max_length=120)
#     email = models.EmailField()
#     address = models.CharField(max_length=120)
#     total = models.ManyToManyField(Cart, default=None)

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cart = models.ForeignKey('Cart', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        price = self.product.price
        self.product.price = price
        print(self.quantity)

        self.total = int(self.quantity) * price

        super(ProductOrder, self).save(*args, **kwargs)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user

    def add_to_cart(self, product_slug):
        product = Product.objects.get(slug=product_slug)
        try:
            preexisting_order = ProductOrder(product=product, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except ProductOrder.DoesNotExist:
            new_order = ProductOrder.objects.create(product=product, cart=self, quantity=1)
            new_order.save()

            def __unicode__(self):
                return self.product_slug

    def remove_from_cart(self, product_slug):
        product = Product.objects.get(slug=product_slug)
        try:
            preexisting_order = ProductOrder.objects.get(product=product, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except ProductOrder.DoesNotExist:
            pass

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    adress = models.CharField(max_length=120)
    products = models.ManyToManyField(ProductOrder, blank=True)

    def __str__(self):
        return self.first_name


    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'