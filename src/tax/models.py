from django.db import models
from .models import *
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from order_orderdetail.models import *
class Tax_MODEL(models.Model):
    """Django Model for State"""

    tax_rate               = models.DecimalField(max_digits=10,decimal_places=2 , default=15  , blank=True , null=True , verbose_name="Tax %")
    divide_one_hundred     = models.DecimalField(max_digits=10,decimal_places=2 , default=100 , blank=True , null=True , verbose_name="100")
    total_service_charges  = models.DecimalField(max_digits=10,decimal_places=2 , default=0   , blank=True , null=True , verbose_name="0")

    class Meta:
        ordering            = ('-tax_rate',)
        verbose_name        = "Tax"
        verbose_name_plural = "Taxs" 
    #
    # 'admin'display the field name on a page
    def __str__(self):
        return str(self.tax_rate)
    #
    # Tax Rate 15%
    @property
    def get_tax_rate_PROPERTY(self): # 15 %
        tax_rate_VAR = str(self.tax_rate) 
        return tax_rate_VAR
    #
    # Tax Amount
    @property
    def get_tax_amount_PROPERTY(self): # SR 
        tax_amount_VAR=0
        products_prices_VAR=0
        
        orderitems =  OrderDetailsMODEL.objects.all()
        for sub in orderitems:
            # Calculation multiply the price of the product by the quantity
            products_prices_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity

        tax_VAR                 = self.tax_rate
        divisor_number_VAR      = self.divide_one_hundred
        tax_amount_VAR =  (100 * 15 )/100
        return tax_amount_VAR
    #
    # Subtotal - The Amount Witheout The Tax Value
    @property
    def get_subtotal_without_tax_PROPERTY(self):
        total_VAR=0
        orderitems = OrderDetailsMODEL.objects.all()
        for sub in orderitems:
            # Calculation multiply the price of the product by the quantity
            total_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity
        return total_VAR
    #
    # Grandtotal - The Amount Withe The Tax Value
    @property
    def get_grandtotal_withe_tax_PROPERTY(self):
        # Grandtotal = get_subtotal_without_tax_PROPERTY + get_tax_amount_PROPERTY + get_total_service_charges_PROPERTY
        grandtotal_withe_tax_VAR=0
        # grandtotal_withe_tax_VAR = self.get_subtotal_without_tax_PROPERTY + self.get_tax_amount_PROPERTY + self.get_total_service_charges_PROPERTY
        grandtotal_withe_tax_VAR = 100                                    + 15                           + 30
        return grandtotal_withe_tax_VAR
    #


    # @property
    # def get_grandtotal_withe_tax_PROPERTY(self):
    #     # Grandtotal = get_subtotal_without_tax_PROPERTY + get_tax_amount_PROPERTY + get_total_service_charges_PROPERTY
    #     amount_includes_tax_VAR=0
    #     products_prices_VAR=0
    #     # orderitems_VAR = OrderDetailsMODEL.objects.all()
    #     # products_prices_VAR = sum([item.OrderDetails_price for item in orderitems_VAR])
    #     orderitems =  OrderDetailsMODEL.objects.all()
    #     for sub in orderitems:
    #         # Calculation multiply the price of the product by the quantity
    #         products_prices_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity

    #     tax_VAR                 = self.tax_rate
    #     divisor_number_VAR      = self.divide_one_hundred
    #     amount_includes_tax_VAR =  (100 * 15 )/100
    #     return amount_includes_tax_VAR
    # #


#     #

    # tax              = models.CharField(max_length=30 , help_text="Enter Tax", verbose_name="Tax1 %")
    # tax_tax          = models.PositiveIntegerField(default=0,blank=True,null=True, verbose_name="tax_tax2 %")
    # tax_price        = models.DecimalField(default=Decimal(0) ,decimal_places=2, max_digits=10)


# class Product(models.Model):
#     name = models.Charfield(max_lenght=50)
#     price = models.DecimalField(decimal_places=2, max_digits=10)
#     tax = models.PositiveIntegerField()
#     tax_accountant = models.ForeignKey(
#         UserModel,
#         on_delete=models.SET_NULL,
#         related_name='user_tax_accountant',
#         null=True,
#         blank=True
#     )



# class Product(models.Model):
#     name = models.Charfield(max_lenght=50)
#     price = models.DecimalField(decimal_places=2, max_digits=10)
#     tax = models.PositiveIntegerField()



# class Cart(models.Model):
#     items = models.ManyToManyField(ProductMODEL, through="CartProduct")

#     def total(self):
#         total = 0.0
#         for item in self.items.all():
#             total += (item.product.prodPrice * item.quantity)
#         return total



# class Store(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     name = models.CharField(max_length=128, blank=True, default="", verbose_name="Name")



# class StoreAnalytics(models.Model):
#     store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, related_name="store_id")
#     sales_sum = models.DecimalField(
#         max_digits=10, decimal_places=2, default=Decimal(0), verbose_name="Sales")
#     tax = models.IntegerField(
#         default=6, validators=[MaxValueValidator(20), MinValueValidator(0)], verbose_name="Tax %"
#     )