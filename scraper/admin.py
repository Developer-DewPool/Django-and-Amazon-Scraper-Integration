from django.contrib import admin

from .models import AmazonPhoneProducts


@admin.register(AmazonPhoneProducts)
class AmazonPhoneProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'rating', 'brand', 'model_name',
                    'operating_system', 'cellular_technology', 'wireless_network_technology')


                    