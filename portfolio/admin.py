from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'name',
        'rating',
        'category',
        'image',
        'image_url',
        'image',
        'url',
    )

    ordering = ('rating',)


admin.site.register(Portfolio, PortfolioAdmin)

