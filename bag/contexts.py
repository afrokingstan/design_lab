from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    vat = 0

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_QUOTE_THRESHOLD:
        quote = total * Decimal(settings.STANDARD_QUOTE_PERCENTAGE / 100)
        free_quote_delta = settings.FREE_QUOTE_THRESHOLD - total
    else:
        quote = 0
        free_quote_delta = 0

    vat = total * Decimal(settings.STANDARD_QUOTE_PERCENTAGE * 0.02)
    grand_total = vat + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'quote': quote,
        'free_quote_delta': free_quote_delta,
        'free_quote_threshold': settings.FREE_QUOTE_THRESHOLD,
        'vat': vat,
        'grand_total': grand_total,
    }

    return context
