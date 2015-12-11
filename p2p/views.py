from django.shortcuts import render
from .models import P2P_accounting

# Create your views here.
def p2p_accounting(request):
    receipt_accting = P2P_accounting.objects.filter( accounting_entry='PO Receipt').filter(item_type='Expense')
    deliver_accting = P2P_accounting.objects.filter( accounting_entry='PO Deliver').filter(item_type='Expense')
    invoice_accting = P2P_accounting.objects.filter( accounting_entry='AP Invoice')
    payment_accting = P2P_accounting.objects.filter( accounting_entry='AP Payment')
    return render(request, 'p2p/p2p_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting,
        'ap_invoice_accting':invoice_accting, 'ap_payment_accting':payment_accting})

def inv_accounting(request):
    receipt_accting = P2P_accounting.objects.filter( accounting_entry='PO Receipt').filter(item_type='Inventory')
    deliver_accting = P2P_accounting.objects.filter( accounting_entry='PO Deliver').filter(item_type='Inventory')
    invoice_accting = P2P_accounting.objects.filter( accounting_entry='AP Invoice')
    payment_accting = P2P_accounting.objects.filter( accounting_entry='AP Payment')
    return render(request, 'p2p/inv_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting,
        'ap_invoice_accting':invoice_accting, 'ap_payment_accting':payment_accting})