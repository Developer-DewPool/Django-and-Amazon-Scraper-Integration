from django.contrib import admin

from .models import AmazonPhoneProducts, InputLinks


@admin.register(AmazonPhoneProducts)
class AmazonPhoneProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ASIN', 'title', 'price', 'rating', 'brand', 'model_name',
                    'operating_system', 'cellular_technology', 'wireless_network_technology')

    search_fields = ('ASIN',)


@admin.register(InputLinks)
class InputLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'scrape',)