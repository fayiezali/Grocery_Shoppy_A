from django.db import models
from .models import *
from decimal import Decimal
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.utils.timezone import now


# Model Proudect
class ProductMODEL(models.Model):
    product_name         = models.CharField(max_length=200)
    product_description  = models.TextField()
    # product_price        = models.DecimalField(max_digits=10,decimal_places=2)
    product_price        = models.DecimalField(max_digits=10,decimal_places=4,default=Decimal('00.00'), blank=True , null=True , verbose_name="Price")
    product_image        = models.ImageField(upload_to="Productes_File_Photo/%Y/%m/%d/")
    product_is_active 	 = models.BooleanField(default=False)
    product_publish_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering            = ('-product_publish_date',)
        verbose_name        = "Product"
        verbose_name_plural = "Products" 

    # 'admin'display the field name on a page
    def __str__(self):
        return self.product_name
