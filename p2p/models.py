from django.db import models


# Create your models here.
class P2P_accounting(models.Model):
    dr_cr = models.CharField (max_length = 6)
    account_description = models.CharField (max_length=25)
    accounting_entry = models.CharField(max_length=15)
    item_type = models.CharField(max_length=10)
    stream = models.CharField(max_length=5)
