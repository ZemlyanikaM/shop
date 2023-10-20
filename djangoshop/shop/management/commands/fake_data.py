from django.core.management.base import BaseCommand
from shop.models import Product, Client, Order
import random


class Command(BaseCommand):
    help = "Generate fake data"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='quantity of fake clients')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        name = []
        clients_ = []
        products_ = []
        orders_ = []

        for i in range(1, count + 1):
            client = Client(name_cl=f'Name{i}',
                            email=f'email{i}@mail.ru',
                            phone=f'{random.randint(89100000000, 89199999999)}',
                            address=f'address{i}')
            client.save()
            clients_.append(client)

        for j in range(1, count + 1):
            product = Product(name_pr=f'product{j}',
                              description_pr=f'description{j}',
                              cost=f'{random.randint(1, 100)}.{random.randint(1, 100)}',
                              quantity=f'{random.randint(1, 10)}',
                              date_add_product=f'05-10-2023')
            product.save()
            products_.append(product)

        total_cost = 0
        for k in range(1, count + 1):
            order = Order(customer=clients_[random.randint(0, count - 1)])
            for m in range(0, count - 1):
                if random.randint(0, 1) == 1:
                    total_cost += float(products_[m].cost)
                    order.total_cost = total_cost
                    order.save()
                    order.products.add(products_[m])
