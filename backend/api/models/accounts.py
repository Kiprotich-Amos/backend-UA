from django.db import models
from django.contrib.auth.models import User



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
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey('Suppliers', on_delete=models.CASCADE)

    def __str__(self):
        return self.po_number

class SupplierPayments(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    purchase_order = models.ForeignKey('PurchaseOrders', on_delete=models.CASCADE, db_column='po_id')
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey('Suppliers', on_delete=models.CASCADE, db_column='supplier_id')

    def __str__(self):
        return f"Payment {self.payment_id} - PO: {self.purchase_order.po_number}"

class PriceSet(models.Model):
    company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
    price_name = models.CharField(max_length=255) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) 
    currency = models.CharField(max_length=3)  # e.g., USD, EUR, KES

    def __str__(self):
        return self.price_name
