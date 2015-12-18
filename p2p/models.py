from django.db import models


# Create your models here.
class P2P_accounting(models.Model):
    DR_OR_CR = ( ('DEBIT','DEBIT'), ('CREDIT','CREDIT'))    
    YES_OR_NO = ((True, 'Yes'), (False, 'No'))
    OE_LINE_FLOW = (('Bill Only', 'Bill Only'),('Bill Only with Inv Interface', 'Bill Only with Inv Interface') )
    ITEM_TYPES = ( ('Expense','Expense'), ('Inventory','Inventory'))    
    dr_cr = models.CharField (max_length = 6, 
                                                    choices = DR_OR_CR,
                                                    blank=False)
    account_description = models.CharField (max_length=30)
    accounting_entry = models.CharField(max_length=25)
    item_type = models.CharField(max_length=20,
                                                            choices= ITEM_TYPES,
                                                            default= 'Expense',
                                                            blank= False)
    stream = models.CharField(max_length=5)
    period_end_accrual = models.BooleanField(
                                                            default = False,
                                                            blank= False,
                                                            choices= YES_OR_NO)
    allow_recon_accounting =  models.BooleanField(
                                                            default = False,
                                                            blank= False,
                                                            choices= YES_OR_NO)
    oe_line_flow = models.CharField (max_length= 30,
                                                            default = 'Bill Only',
                                                            choices= OE_LINE_FLOW)
