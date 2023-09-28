from django.db import models
from .models import *
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from order_orderdetail.models import *
from django.contrib.auth import get_user_model
class Tax_MODEL(models.Model):
    """Django Model for State"""

    tax_rate               = models.DecimalField(max_digits=10,decimal_places=2 , default=15  , blank=True , null=True , verbose_name="Tax %")
    divide_one_hundred     = models.DecimalField(max_digits=10,decimal_places=2 , default=100 , blank=True , null=True , verbose_name="100")
    service_charges        = models.DecimalField(max_digits=10,decimal_places=2 , default=0   , blank=True , null=True , verbose_name="Service Charges")
    tax_accountant         = models.ForeignKey( User, on_delete=models.CASCADE, related_name='user_tax_accountant',null=True, blank=True , verbose_name="Tax Accountant")

    # Create your models here.
    class Meta:
        ordering            = ('-tax_rate',)
        verbose_name        = "Tax"
        verbose_name_plural = "Taxs" 
    #
    # 'admin'display the field name on a page
    def __str__(self):
        return str(self.tax_rate)
    #
    #
    @property
    def get_current_user_id_PROPERTY(self): # 
        current_user_id_VAR = OrderMODEL.objects.all()
        for user_id in current_user_id_VAR:
            # 
            return user_id.order_user.id
    #
    #
    @property
    def get_current_user_username_PROPERTY(self): # 
        current_user_username_VAR = OrderMODEL.objects.all()
        for user_username in current_user_username_VAR:
            # 
            return user_username.order_user.username


    # @property
    # def get_current_order_PROPERTY(self): # 


        # Tax Amount
    @property
    def get_tax_amount_PROPERTY(self): # SR 
        tax_amount_VAR=0
        products_prices_VAR=0
        order_VAR = OrderMODEL.objects.get(
            order_user=self.get_current_user_id_PROPERTY , 
            order_is_finished=False)
        orderitems_VAR = OrderDetailsMODEL.objects.all().filter(OrderDetails_order=order_VAR)

        for item in orderitems_VAR:
            # Calculation multiply the price of the product by the quantity
            products_prices_VAR += item.OrderDetails_price 

        tax_VAR                 = self.tax_rate
        divisor_number_VAR      = self.divide_one_hundred
        tax_amount_VAR =  (products_prices_VAR * tax_VAR )/divisor_number_VAR
        return tax_amount_VAR
    #
    #
    @property
    def get_amount_of_products_witheout_VAT_Tax_PROPERTY(self):
        products_prices_VAR=0
        order_VAR = OrderMODEL.objects.get(
            order_user=self.get_current_user_id_PROPERTY , 
            order_is_finished=False)
        orderitems_VAR = OrderDetailsMODEL.objects.all().filter(OrderDetails_order=order_VAR)

        for item in orderitems_VAR:
            # Calculation multiply the price of the product by the quantity
            products_prices_VAR += item.OrderDetails_price 
        return products_prices_VAR
    #
    # Service Charges
    @property
    def get_service_charges_PROPERTY(self): # 15 %
        service_charges_VAR = str(self.service_charges) 
        return service_charges_VAR
    #
    #
    # Tax Rate 15%
    @property
    def get_tax_rate_PROPERTY(self): # 15 %
        tax_rate_VAR = str(self.tax_rate) 
        return tax_rate_VAR
    #
    # Subtotal - The Amount Witheout The Tax Value
    @property
    def get_subtotal_without_tax_PROPERTY(self):
        subtotal_without_tax=0
        subtotal_without_tax=self.get_amount_of_products_witheout_VAT_Tax_PROPERTY + self.get_tax_amount_PROPERTY + self.service_charges
        return subtotal_without_tax
    # 
    #
    @property
    def get_discount_PROPERTY(self):
        discount_amount_VAR =Decimal(0.00) 
        discount_amount_VAR =Decimal(05.00)
        return discount_amount_VAR
    #
    #
    # 
    @property
    def get_grandtotal_withe_tax_and_discount_PROPERTY(self):
        #
        grandtotal_withe_tax_discount_VAR=0.00
        #
        grandtotal_withe_tax_discount_VAR = self.get_subtotal_without_tax_PROPERTY - self.get_discount_PROPERTY
        #
        return grandtotal_withe_tax_discount_VAR














#     #

# class Product_Tax(models.Model):
#     name           = models.CharField(max_length=50)
#     price          = models.DecimalField(decimal_places=2, max_digits=10)
#     tax            = models.PositiveIntegerField()
#     tax_accountant = models.ForeignKey( User, on_delete=models.SET_NULL, related_name='user_tax_accountant',null=True, blank=True )



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