from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ChartOfAccounts(models.Model):
    ACCOUNT_TYPES = (
        ('Asset', 'Asset'),
        ('Liability', 'Liability'),
        ('Equity', 'Equity'),
        ('Revenue', 'Revenue'),
        ('Expense', 'Expense'),
    )

    account_name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPES)
    parent_account = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.account_name

class GeneralLedger(models.Model):
    transaction_id = models.CharField(max_length=200, null= False, unique=True)  # Assuming transaction_item exists and has transaction_id
    account = models.ForeignKey('ChartOfAccounts', on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ledger Entry {self.ledger_id} - Account: {self.account}"    

class PurchaseOrders(models.Model):
    company = models.ForeignKey('api.Company', on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.po_number

class SupplierPayments(models.Model):
    company = models.ForeignKey('api.Company', on_delete=models.CASCADE)
    purchase_order = models.ForeignKey('PurchaseOrders', on_delete=models.CASCADE, db_column='po_id')
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} - PO: {self.purchase_order.po_number}"

class PriceSet(models.Model):
    company_user = models.ForeignKey('api.CompanyUser', on_delete=models.CASCADE)
    price_name = models.CharField(max_length=255) 
    company = models.ForeignKey('api.Company', on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) 
    currency = models.CharField(max_length=3)  # e.g., USD, EUR, KES

    def __str__(self):
        return self.price_name


    
class AccountsDetails(models.Model):
    account_name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=100, blank=True, null=True)
    account_code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    account_currency = models.CharField(max_length=10, blank=True, null=True)
    account_opening = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company_user = models.ForeignKey('api.CompanyUser', on_delete=models.CASCADE, db_column='company_user_id')
    company = models.ForeignKey('api.Company', on_delete=models.CASCADE, db_column='company_id')

    def __str__(self):
        return self.account_name

class TransactionItem(models.Model):
    transaction_code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey('api.Company', on_delete=models.CASCADE, db_column='company_id')
    item_inventory = models.ForeignKey('api.ItemInventory', on_delete=models.CASCADE, db_column='item_inventory_id')
    # broker_inventory = models.ForeignKey('api.BrokerInventory', on_delete=models.CASCADE, db_column='broker_inventory_id')

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
    company = models.ForeignKey('api.Company', on_delete=models.CASCADE, db_column='company_id')
    item_inventory = models.ForeignKey('api.ItemInventory', on_delete=models.CASCADE, db_column='item_inventory_id')
    transaction = models.ForeignKey('TransactionItem', on_delete=models.CASCADE, db_column='transaction_id')

    def __str__(self):
        return f"Invoice {self.charges_invoice_id}"
    