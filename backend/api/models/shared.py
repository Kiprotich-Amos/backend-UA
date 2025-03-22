from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# common shared models file here for

class Role(models.Model):
    role_name = models.CharField(max_length=100)
    role_description = models.CharField(max_length=255)

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_type = models.CharField(max_length=100)
    company_kra_pin = models.CharField(max_length=100, unique=True, null=False)
    company_contact = models.CharField(max_length=155)
    company_mail = models.EmailField(max_length=200, unique=True)
    company_address = models.CharField(max_length=100)
    company_approval = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_companies') # added modified_by field
    # class Meta:
    #     unique_together = ('user', 'company')

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        # Access the user making the change from kwargs if available
        user = kwargs.pop('modified_user', None) # pop user from kwargs so save method works as normal

        if user:
            self.modified_by = user

        super().save(*args, **kwargs)


class CompanyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user_role = models.ForeignKey(Role,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'company')

    def __str__(self):
        return f"{self.user.username} - {self.company.company_name}"

class ConsignmentInventory(models.Model):
    consignment_no = models.CharField(max_length=255) 
    delivery_no = models.CharField(max_length=255) 
    company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    received_at = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return f"Consignment: {self.consignment_no}, Delivery: {self.delivery_no}"
    
class ItemInventoryTransaction(models.Model):
    company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE)
    item_inventory = models.ForeignKey('api.ItemInventory', on_delete=models.CASCADE)
    broker = models.CharField(max_length=255, blank=True, null=True)  
    buyer = models.CharField(max_length=255, blank=True, null=True)  
    status = models.CharField(max_length=50)  
    created_at = models.DateTimeField(auto_now_add=True)  
    sold_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Transaction for {self.item_inventory}"
