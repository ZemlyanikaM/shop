from django.contrib import admin
from django.contrib import admin
from .models import Product, Client, Order


@admin.action(description="reset count")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.action(description="order paid")
def is_paid(modeladmin, request, queryset):
    queryset.update(is_paid=True)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_pr', 'quantity', 'cost']
    ordering = ['name_pr', '-quantity']
    list_filter = ['date_add_product', 'cost']
    search_fields = ['name_pr', 'description_pr']
    search_help_text = 'Search product by name'
    actions = [reset_quantity]
    readonly_fields = ['date_add_product']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name_pr'],
            },
        ),
        (
            'specialty',
            {
                'classes': ['collapse'],
                'description': 'Product description',
                'fields': ['description_pr'],
            },
        ),
        (
            'bookkeeping',
            {
                'fields': ['cost', 'quantity'],
            },
        ),

    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_cl', 'phone']
    ordering = ['id']
    search_fields = ['name_cl', 'phone']
    search_help_text = 'Search client by name or phone'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_cost', 'is_paid']
    ordering = ['-id']
    list_filter = ['date_create_order', 'total_cost', 'is_paid']
    search_fields = ['date_create_order']
    search_help_text = 'Search order by date'
    actions = [is_paid]
    readonly_fields = ['date_create_order']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Products',
            {
                'classes': ['collapse'],
                'description': 'Products',
                'fields': ['products'],
            },
        ),
        (
            'bookkeeping',
            {
                'fields': ['total_cost', 'is_paid', ],
            },
        ),

    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

# Register your models here.
