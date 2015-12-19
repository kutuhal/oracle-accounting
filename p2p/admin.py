from django.contrib import admin
from p2p.models import  P2P_accounting

# Register your models here.

class AccountingAdmin(admin.ModelAdmin):
    fields = ['dr_cr', 'account_description', 'accounting_entry','item_type','period_end_accrual',
    	'allow_recon_accounting', 'journal_source','journal_category','defaults_from', 'accounting_class',
    	'notes']
    list_display = ('dr_cr', 'account_description', 'accounting_entry','item_type','period_end_accrual',
    	'allow_recon_accounting', 'journal_source', 'journal_category','defaults_from','accounting_class')

admin.site.register(P2P_accounting, AccountingAdmin)