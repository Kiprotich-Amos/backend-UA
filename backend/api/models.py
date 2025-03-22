from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager, AbstractUser


class CustomUserManager(UserManager):
    def create_superuser(self, email, first_name, last_name, mobile_no, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.model(email=email, first_name=first_name, last_name=last_name, mobile_no=mobile_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile_no']

    def __str__(self):
        return self.email
    
# class Role(models.Model):
#     role_name = models.CharField(max_length=100)
#     role_description = models.CharField(max_length=255)
    
# class Company(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=200)
#     company_type = models.CharField(max_length=100)
#     company_kra_pin = models.CharField(max_length=100, unique=True, null=False)
#     company_contact = models.CharField(max_length=155)
#     company_mail = models.EmailField(max_length=200, unique=True)
#     company_address = models.CharField(max_length=100)
#     company_approval = models.BooleanField(default=False)
#     last_modified = models.DateTimeField(auto_now=True)
#     modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_companies') # added modified_by field

#     def __str__(self):
#         return self.company_name

#     def save(self, *args, **kwargs):
#         # Access the user making the change from kwargs if available
#         user = kwargs.pop('modified_user', None) # pop user from kwargs so save method works as normal

#         if user:
#             self.modified_by = user

#         super().save(*args, **kwargs)

# class CompanyUser(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     user_role = models.ForeignKey(Role,on_delete=models.CASCADE)
#     status = models.BooleanField(default=True)  
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('user', 'company')

#     def __str__(self):
#         return f"{self.user.username} - {self.company.company_name}"
    
# class ChartOfAccounts(models.Model):
#     ACCOUNT_TYPES = (
#         ('Asset', 'Asset'),
#         ('Liability', 'Liability'),
#         ('Equity', 'Equity'),
#         ('Revenue', 'Revenue'),
#         ('Expense', 'Expense'),
#     )

#     account_name = models.CharField(max_length=255)
#     account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPES)
#     parent_account = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.account_name

# class GeneralLedger(models.Model):
#     transaction_id = models.CharField(max_length=200, null= False, unique=True)  # Assuming transaction_item exists and has transaction_id
#     account = models.ForeignKey('ChartOfAccounts', on_delete=models.CASCADE)
#     debit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
#     credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Ledger Entry {self.ledger_id} - Account: {self.account}"    

# class PurchaseOrders(models.Model):
#     company = models.ForeignKey('Company', on_delete=models.CASCADE)
#     po_number = models.CharField(max_length=50, unique=True)
#     total_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
#     STATUS_CHOICES = (
#         ('Pending', 'Pending'),
#         ('Completed', 'Completed'),
#         ('Cancelled', 'Cancelled'),
#     )
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)
#     supplier = models.ForeignKey('Suppliers', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.po_number

# class SupplierPayments(models.Model):
#     company = models.ForeignKey('Company', on_delete=models.CASCADE)
#     purchase_order = models.ForeignKey('PurchaseOrders', on_delete=models.CASCADE, db_column='po_id')
#     amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     supplier = models.ForeignKey('Suppliers', on_delete=models.CASCADE, db_column='supplier_id')

#     def __str__(self):
#         return f"Payment {self.payment_id} - PO: {self.purchase_order.po_number}"

# class PriceSet(models.Model):
#     company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
#     price_name = models.CharField(max_length=255) 
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2) 
#     currency = models.CharField(max_length=3)  # e.g., USD, EUR, KES

#     def __str__(self):
#         return self.price_name

# class ConsignmentInventory(models.Model):
#     consignment_no = models.CharField(max_length=255) 
#     delivery_no = models.CharField(max_length=255) 
#     company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     received_at = models.DateTimeField(null=True, blank=True) 

#     def __str__(self):
#         return f"Consignment: {self.consignment_no}, Delivery: {self.delivery_no}"

# class ItemInventory(models.Model):
    consignment_inventory = models.ForeignKey(ConsignmentInventory, on_delete=models.CASCADE)
    company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
    item_invoice_no = models.CharField(max_length=255)  
    item_grade = models.CharField(max_length=100)  
    item_no_of_bags = models.PositiveIntegerField()
    item_tare = models.DecimalField(max_digits=10, decimal_places=2) 
    item_pallet_weight = models.DecimalField(max_digits=10, decimal_places=2) 
    item_net_weight = models.DecimalField(max_digits=10, decimal_places=2)  
    item_gross_weight = models.DecimalField(max_digits=10, decimal_places=2)
    item_comment = models.TextField(blank=True, null=True)
    warranty_no = models.CharField(max_length=255, blank=True, null=True)  

    def __str__(self):
        return f"Invoice: {self.item_invoice_no}, Consignment: {self.consignment_inventory.consignment_no}"

# class ItemInventoryTransaction(models.Model):
#     company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
#     item_inventory = models.ForeignKey(ItemInventory, on_delete=models.CASCADE)
#     broker = models.CharField(max_length=255, blank=True, null=True)  
#     buyer = models.CharField(max_length=255, blank=True, null=True)  
#     status = models.CharField(max_length=50)  
#     created_at = models.DateTimeField(auto_now_add=True)  
#     sold_at = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return f"Transaction for {self.item_inventory}"

# class GeneralCargo(models.Model):
#     consignment_no = models.CharField(max_length=255)  
#     kra_no = models.CharField(max_length=255) 
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
#     transporter = models.CharField(max_length=255, blank=True, null=True)  
#     no_bags = models.PositiveIntegerField()
#     units_measure = models.CharField(max_length=50)  
#     net_weight = models.DecimalField(max_digits=10, decimal_places=2)  
#     gross_weight = models.DecimalField(max_digits=10, decimal_places=2)  
#     status_one = models.CharField(max_length=50)  
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Consignment: {self.consignment_no}"

# class CargoItemRelease(models.Model):
#     general_cargo = models.ForeignKey(GeneralCargo, on_delete=models.CASCADE)
#     company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
#     transporter = models.CharField(max_length=255, blank=True, null=True)  
#     no_bags = models.PositiveIntegerField()
#     net_weight = models.DecimalField(max_digits=10, decimal_places=2)  
#     gross_weight = models.DecimalField(max_digits=10, decimal_places=2)  
#     status = models.CharField(max_length=50)  
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Release for Cargo: {self.general_cargo.consignment_no}"
    
# class OperationTable(models.Model):
#     company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
#     name_operation = models.CharField(max_length=255)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     price_set = models.ForeignKey(PriceSet, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name_operation
    
class AccountsDetails(models.Model):
    account_name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=100, blank=True, null=True)
    account_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    account_currency = models.CharField(max_length=10, blank=True, null=True)
    account_opening = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company_user = models.ForeignKey('CompanyUser', on_delete=models.CASCADE, db_column='company_user_id')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, db_column='company_id')

    def __str__(self):
        return self.account_name

class TransactionItem(models.Model):
    transaction_code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, db_column='company_id')
    item_inventory = models.ForeignKey('ItemInventory', on_delete=models.CASCADE, db_column='item_inventory_id')
    broker_inventory = models.ForeignKey('BrokerInventory', on_delete=models.CASCADE, db_column='broker_inventory_id')

    def __str__(self):
        return self.transaction_code
    
class ChargesInvoice(models.Model):
    contract_name = models.CharField(max_length=255, blank=True, null=True)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    item_description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    units = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, db_column='company_id')
    item_inventory = models.ForeignKey('ItemInventory', on_delete=models.CASCADE, db_column='item_inventory_id')
    transaction = models.ForeignKey('TransactionItem', on_delete=models.CASCADE, db_column='transaction_id')

    def __str__(self):
        return f"Invoice {self.charges_invoice_id}"