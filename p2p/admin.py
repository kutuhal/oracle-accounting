from django.contrib import admin
from p2p.models import  P2P_accounting

# Register your models here.

class AccountingAdmin(admin.ModelAdmin):
    fields = ['dr_cr', 'account_description', 'accounting_entry','item_type']
    list_display = ('dr_cr', 'account_description', 'accounting_entry','item_type')

admin.site.register(P2P_accounting, AccountingAdmin)