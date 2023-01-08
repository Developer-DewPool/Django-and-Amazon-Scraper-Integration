from django.db import models
from django.utils.translation import gettext as _


class AmazonPhoneProducts(models.Model):
    link = models.URLField(null=True, blank=True, verbose_name=_('link'))
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('title'))
    price = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('price'))
    rating = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('rating'))
    brand = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('brand'))
    model_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('model name'))
    operating_system = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('operating system'))
    cellular_technology = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('cellular technology'))
    wireless_network_technology = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('wireless network technology'))
    about = models.TextField(null=True, blank=True, verbose_name=_('about'))