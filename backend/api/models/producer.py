from django.db import models
from django.contrib.auth import get_user_model
# from .shared import CompanyUser, ConsignmentInventory

User = get_user_model()
# create producer models here

class ItemInventory(models.Model):
    consignment_inventory = models.ForeignKey('api.ConsignmentInventory', on_delete=models.CASCADE)
    company_user = models.ForeignKey('api.CompanyUser', on_delete=models.CASCADE)
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
