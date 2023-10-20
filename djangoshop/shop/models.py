from django.db import models


class Client(models.Model):
    name_cl = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'name: {self.name_cl}, email: {self.email},  phone: {self.phone}, address: {self.address}'


class Product(models.Model):
    name_pr = models.CharField(max_length=50)
    description_pr = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_add_product = models.DateField(auto_now_add=True)
    image_pr = models.ImageField(upload_to="images/")

    def __str__(self):
        return f'Product: {self.name_pr},  quantity: {self.quantity}, cost: {self.cost},  ' \
               f'description: {self.description_pr}, product creation date: {self.date_add_product}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    date_create_order = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'name_of_client: {self.customer.name_cl} \nproducts: {self.products.all()} ' \
               f'\ntotal_cost: {self.total_cost} \ndate_create_order: {self.date_create_order}'
