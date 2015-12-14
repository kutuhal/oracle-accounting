from django.db import models


# Create your models here.
class P2P_accounting(models.Model):
    DR_OR_CR = ( ('DEBIT','DEBIT'), ('CREDIT','CREDIT'))    
    YES_OR_NO = ((True, 'Yes'), (False, 'No'))
    dr_cr = models.CharField (max_length = 6, 
                                                    choices = DR_OR_CR,
                                                    blank=False)
    account_description = models.CharField (max_length=25)
    accounting_entry = models.CharField(max_length=15)
    item_type = models.CharField(max_length=20)
    stream = models.CharField(max_length=5)
    period_end_accrual = models.BooleanField(
                                                            default = False,
                                                            blank= False,
                                                            choices= YES_OR_NO)
    allow_recon_accounting =  models.BooleanField(
                                                            default = False,
                                                            blank= False,
                                                            choices= YES_OR_NO)
