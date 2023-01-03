from django.db import models

#makemigrations = create changes and store in a file 
#migrate= apply the pending changes

# Create your models here.

class project_table(models.Model):
    name=models.CharField(null=False,max_length=100)
    
    def __str__(self):
        return self.name

class vendor_table(models.Model):
    name=models.CharField(null=False,max_length=100)

    def __str__(self):
        return self.name
    
class expired_table(models.Model):
    project=models.ForeignKey(project_table,on_delete=models.CASCADE)
    vendor=models.ForeignKey(vendor_table,on_delete=models.CASCADE)
    PO=models.CharField(max_length=20)
    oldPO=models.CharField(null=True, blank=True,max_length=20)
    typePO=models.CharField(null=True, blank=True,max_length=20)
    desc=models.CharField(null=True, blank=True,max_length=100)
    price=models.CharField(null=True, blank=True,max_length=100)
    startdate=models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    enddate=models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    PR=models.CharField(null=True, blank=True,max_length=20)
    PRdate=models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    BC1=models.BooleanField(null=True,default=False)
    BC2=models.BooleanField(null=True,default=False)
    BC3=models.BooleanField(null=True,default=False)
    BC4=models.BooleanField(null=True,default=False)
    PMC1=models.BooleanField(null=True,default=False)
    PMC2=models.BooleanField(null=True,default=False)
    PMC3=models.BooleanField(null=True,default=False)
    PMC4=models.BooleanField(null=True,default=False)
    
    class Meta:
        db_table="expireddb"
    def __str__(self):
        return self.PO
    
class basetable(models.Model):
    project=models.ForeignKey(project_table,on_delete=models.CASCADE)
    vendor=models.ForeignKey(vendor_table,on_delete=models.CASCADE)
    PO=models.CharField(max_length=20)
    oldPO=models.CharField(null=True, blank=True,max_length=20)
    typePO=models.CharField(null=True, blank=True,max_length=20)
    desc=models.CharField(null=True, blank=True,max_length=100)
    price=models.CharField(null=True, blank=True,max_length=100)
    startdate=models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    enddate=models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    PR=models.CharField(null=True, blank=True,max_length=20)
    PRdate=models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    BC1=models.BooleanField(null=True,default=False)
    BC2=models.BooleanField(null=True,default=False)
    BC3=models.BooleanField(null=True,default=False)
    BC4=models.BooleanField(null=True,default=False)
    PMC1=models.BooleanField(null=True,default=False)
    PMC2=models.BooleanField(null=True,default=False)
    PMC3=models.BooleanField(null=True,default=False)
    PMC4=models.BooleanField(null=True,default=False)
    
    class Meta:
        db_table="maindb"
    def __str__(self):
        return self.PO
    