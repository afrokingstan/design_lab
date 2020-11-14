from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'vat',
                       'grand_total',)

    fields = ('order_number','project_name','project_description', 'date', 'project_owner_full_name',
              'project_owner_email', 'project_owner_phone_number',
              'full_name', 'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'vat',
              'order_total', 'grand_total',)

    list_display = ('order_number','project_name', 'project_description',
                    'project_owner_full_name', 'project_owner_phone_number',
                    'project_owner_email', 'date', 'order_total',
                    'vat', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)