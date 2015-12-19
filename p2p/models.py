from django.db import models


# Create your models here.
class P2P_accounting(models.Model):
    DR_OR_CR = ( ('DEBIT','DEBIT'), ('CREDIT','CREDIT'))    
    YES_OR_NO = ((True, 'Yes'), (False, 'No'))
    OE_LINE_FLOW = (('Bill Only', 'Bill Only'),('Bill Only with Inv Interface', 'Bill Only with Inv Interface') )
    ITEM_TYPES = ( ('Expense','Expense'), ('Inventory','Inventory'), ('Not Relevant', 'Not Relevant') )
    JOURNAL_SOURCE =  ( ('Assets','Assets'), ('Payables','Payables'),
                                                    ('Receivables','Receivables'), ('Cost Management','Cost Management'),
                                                    ('Treasury','Treasury') , ('Cash Management', 'Cash Management'),
                                                    ('Revaluation','Revaluation'), ('Spreadsheet', 'Spreadsheet'), )
    JOURNAL_CATEGORY = (
                                                    # Payables Categories
                                                    ('Payments', 'Payments'),('Standard Invoices','Purchase Invoices'),
                                                    ('Reconciled Payments','Reconciled Payments'),
                                                    # Receivables Categories 
                                                    ('Sales Invoices', 'Sales Invoices'),('Debit Memo','Debit Memo'), ('Credit Memo','Credit Memo'),
                                                    ('Receipts','Receipts'), ('Misc Receipts', 'Misc Receipts'),
                                                    #FA Categories
                                                    ('Addition','Addition'), ('CIP Addition','CIP Addition'),
                                                    ('Transfer','Transfer'), ('CIP Transfer','CIP Transfer'), 
                                                    ('Adjustment','Adjustment'), ('CIP Adjustment','CIP Adjustment'),
                                                    ('Reclass', 'Reclass'),('CIP Reclassification', 'CIP Reclassification'),
                                                    ('Depreciation','Depreciation'), ('Retirement','Retirement'),
                                                    # Cost Management Categories
                                                    ('Receiving','Receiving'), ('WIP', 'WIP'), ('Inventory', 'Inventory'),
                                                    # Cash Management Sources
                                                    ( 'Bank Transfer', 'Bank Transfer'),
                                                    # GL Journals Sources
                                                    ('Revaluation', 'Revaluation'),
                                                    )
    ACCOUNTING_CLASS = (
                                                    # Receivables related
                                                    ('Cash', 'Cash'),('Receivable', 'Receivable'),('Remitted Cash', 'Remitted Cash'),
                                                    ('Revenue', 'Revenue'),
                                                    # Cost Management related
                                                    ('Receiving Inspection', 'Receiving Inspection'),('Accrual','Accrual'),('Charge','Charge'),
                                                    ('Inventory Valuation', 'Inventory Valuation'),( 'WIP Valuation', 'WIP Valuation'),
                                                    ('Offset','Offset'),
                                                    #Payables related
                                                    ('Liability','Liability'),('Cash Clearing', 'Cash Clearing'),('Invoice Price Variance','Invoice Price Variance'),
                                                    ('Item Expense','Item Expense'),
                                                    )
    DEFAULTS_FROM        = (
                                                    # Cost Management & Purchasing
                                                    ('Purchasing Options', 'Purchasing Options'),('Receiving Options', 'Receiving Options'),
                                                    )
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
                                                            blank= True,
                                                            choices= YES_OR_NO)
    oe_line_flow = models.CharField (max_length= 30, blank = False,
                                                            default = 'Bill Only',
                                                            choices= OE_LINE_FLOW)
    journal_source = models.CharField (max_length= 30, null = True,
                                                            choices= JOURNAL_SOURCE)
    journal_category = models.CharField (max_length= 30, null = True,
                                                            choices= JOURNAL_CATEGORY)
    defaults_from = models.CharField (max_length= 30, null = True
                                                            )
    accounting_class = models.CharField(max_length= 30, null = True,
                                                            choices= ACCOUNTING_CLASS)
    notes = models.CharField (max_length= 100, blank = True, default = 'NA')
    

