from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import logging
from .models import Client, Product, Order
from datetime import datetime, timedelta
from .forms import ProductForm, GetProductById

logger = logging.getLogger(__name__)


def products(request):
    logger.info(f'products request received')
    products = Product.objects.all()
    res = ''
    for product in products:
        res += str(product)
    return HttpResponse(res)


def clients(request):
    logger.info(f'Clients request received')
    cls = Client.objects.all()
    res = ''
    for client in cls:
        res += str(client)

    return HttpResponse(res)


def orders(request):
    logger.info(f'Orders request received')
    orders = Order.objects.all()
    res = ''
    for order in orders:
        res += str(order)
    return HttpResponse(res)


def clients_sorted_products(request, id_client: int, days: int):
    products_set = []
    now = datetime.now()
    before = now - timedelta(days=days)
    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(customer=client, date_create_order__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in products_set:
                products_set.append(product)

    return render(request, 'shop/clients_sorted_products.html',
                  {'client': client, 'products_set': products_set, 'days': days})


def client_orders(request, id_client: int):
    products = {}
    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(buyer=client).all()

    for order in orders:
        products[order.id] = str(order.products.all()).replace('<QuerySet [<', '').replace('>]>', '').split('>, <')

    return render(request, 'shop/client_orders.html', {'client': client, 'orders': orders, 'products': products})


def product(request, id_pr: int):
    product = Product.objects.filter(pk=id_pr).first()
    context = {
        "product": product

    }
    return render(request, "shop/product.html", context=context)


def edit_product(request):
    if request.method == "POST":
        form = GetProductById(request.POST, request.FILES)
        if form.is_valid():
            id_pr = request.POST['id_pr']

            return redirect("product", id_pr)
    else:
        form = GetProductById()

    context = {
        "form": form
    }
    return render(request, "shop/edit_product_form.html", context=context)


def product_form(request, id_pr: int):
    product = get_object_or_404(Product, pk=id_pr)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name_pr = request.POST["name_pr"]
            product.description_pr = request.POST["description_pr"]
            product.cost = request.POST["cost"]
            product.quantity = request.POST["quantity"]
            image = form.cleaned_data['image']
            if "image" in request.FILES:
                product.image_pr = request.FILES["image"]
            product.save()
            logger.info(f"Product {product.name_pr} is changed successfully")
            return redirect("product", id_pr=product.id)
    else:
        form = ProductForm()

    context = {
        "form": form,
        "product": product,
    }
    return render(request, "shop/product_form.html", context=context)


def edit_product_by_id(request):
    if request.method == "POST":
        form = GetProductById(request.POST, request.FILES)
        if form.is_valid():
            id_pr = request.POST['id_pr']
            return redirect("product_form", id_pr)
    else:
        form = GetProductById()

    context = {
        "form": form
    }
    return render(request, "shop/edit_product_form.html", context=context)
