from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_QUOTE_THRESHOLD:
        quote = total * Decimal(settings.STANDARD_QUOTE_PERCENTAGE / 100)
        free_quote_delta = settings.FREE_QUOTE_THRESHOLD - total
    else:
        quote = 0
        free_quote_delta = 0

    grand_total = quote + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'quote': quote,
        'free_quote_delta': free_quote_delta,
        'free_quote_threshold': settings.FREE_QUOTE_THRESHOLD,
        'grand_total': grand_total,
    }

    return context