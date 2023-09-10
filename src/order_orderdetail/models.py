from django.db import models
from .models import *
from product.models import *
from track_shipment.models import *
from decimal import Decimal
from django.contrib.auth.models import User # إستيراد اسم المستخدم
#
#
class OrderMODEL(models.Model):
    order_user        = models.ForeignKey(User , on_delete = models.CASCADE)
    order_order_date  = models.DateTimeField(auto_now_add=True)
    order_details     = models.ManyToManyField(ProductMODEL , through='OrderDetailsMODEL')
    order_is_finished = models.BooleanField(default=False)
    class Meta:
        ordering = ('-order_order_date',)
        verbose_name = "Order"
        verbose_name_plural = "Orders" 

    # 'admin'display the field name on a page
    # \: write code of more than 1 line in the Python interpreter
    def __str__(self):
        return  'User Name: ' + self.order_user.username + '-' \
                'Order Id: ' + str(self.id) 
#
#
#










class OrderDetailsMODEL(models.Model):
    OrderDetails_product  = models.ForeignKey(ProductMODEL , on_delete = models.CASCADE)
    OrderDetails_order    = models.ForeignKey(OrderMODEL   , on_delete = models.CASCADE)
    OrderDetails_price    = models.DecimalField(max_digits=10,decimal_places=2)
    OrderDetails_quantity = models.IntegerField()
    class Meta:
        ordering = ('-OrderDetails_order',)
        verbose_name = "Order Detail"
        verbose_name_plural = "Order Details" 

    # 'admin'display the field name on a page
    # \: write code of more than 1 line in the Python interpreter
    def __str__(self):
        return  'User Name : ' + str(self.OrderDetails_order.order_user) + ' - ' +\
                'Product: ' + self.OrderDetails_product.product_name + ' - ' +\
                'Order Id: ' + str(self.OrderDetails_order.id)

from django.db import models
from .models import *
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.utils.timezone import now


# class ShipmentTrackMODEL(models.Model):
#     shipment_track_user              = models.ForeignKey(User , on_delete = models.CASCADE)
#     shipment_track_order_id          = models.ForeignKey(OrderMODEL, on_delete=models.CASCADE)
#     shipment_track_confirmed_order   = models.BooleanField(default=False)
#     shipment_track_Processing_order  = models.BooleanField(default=False)
#     shipment_track_dispatch_product  = models.BooleanField(default=False)
#     shipment_track_delivery          = models.BooleanField(default=False)
#     shipment_track_Product_delivered = models.BooleanField(default=False)
    
#     class Meta: 
#         ordering = ('-shipment_track_order_id',)
#         verbose_name = "Shipment Track"
#         verbose_name_plural = "Shipment Tracs" 

#     # 'admin'display the field name on a page
#     # \: write code of more than 1 line in the Python interpreter
#     def __str__(self):
#         return  'User Name: ' + self.shipment_track_user.username + '-' \
#                 'Order ID: ' + str(self.shipment_track_order_id) 
# #
