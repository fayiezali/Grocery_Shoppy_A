from django.db import models
from product.models import *
from django.contrib.auth.models import User # إستيراد اسم المستخدم
#
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
