from django.db import models
from .models import User
from .producer import ItemInventory
from .shared import Company, CompanyUser
from .accounts import PriceSet

# create warehouse models here

class GeneralCargo(models.Model):
    consignment_no = models.CharField(max_length=255)  
    kra_no = models.CharField(max_length=255) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
    transporter = models.CharField(max_length=255, blank=True, null=True)  
    no_bags = models.PositiveIntegerField()
    units_measure = models.CharField(max_length=50)  
    net_weight = models.DecimalField(max_digits=10, decimal_places=2)  
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2)  
    status_one = models.CharField(max_length=50)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consignment: {self.consignment_no}"

class CargoItemRelease(models.Model):
    general_cargo = models.ForeignKey(GeneralCargo, on_delete=models.CASCADE)
    company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
    transporter = models.CharField(max_length=255, blank=True, null=True)  
    no_bags = models.PositiveIntegerField()
    net_weight = models.DecimalField(max_digits=10, decimal_places=2)  
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2)  
    status = models.CharField(max_length=50)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Release for Cargo: {self.general_cargo.consignment_no}"
    
class OperationTable(models.Model):
    company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
    name_operation = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price_set = models.ForeignKey(PriceSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_operation
    