from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# create warehouse models here

class GeneralCargo(models.Model):
    consignment_no = models.CharField(max_length=255)  
    kra_no = models.CharField(max_length=255) 
    company = models.ForeignKey('api.Company', on_delete=models.CASCADE)
    company_user = models.ForeignKey('api.CompanyUser', on_delete=models.CASCADE)
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
    company_user = models.ForeignKey('api.CompanyUser', on_delete=models.CASCADE)
    transporter = models.CharField(max_length=255, blank=True, null=True)  
    no_bags = models.PositiveIntegerField()
    net_weight = models.DecimalField(max_digits=10, decimal_places=2)  
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2)  
    status = models.CharField(max_length=50)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Release for Cargo: {self.general_cargo.consignment_no}"
    
class OperationTable(models.Model):
    company_user = models.ForeignKey('api.CompanyUser', on_delete=models.CASCADE)
    name_operation = models.CharField(max_length=255)
    company = models.ForeignKey('api.Company', on_delete=models.CASCADE)
    price_set = models.ForeignKey('api.PriceSet', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_operation
    
class Contract(models.Model):
    contract_name = models.CharField(max_length=255)
    contract_client = models.ForeignKey('api.Company', max_length=100)
    contract_duration =models.CharField(max_length=100)
    expected_cargo = models.TextField(max_length=255)
    contract_unit_price= models.DecimalField(10,2)
    contract_start = models.DateField()