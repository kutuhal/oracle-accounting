from django.shortcuts import render
from .models import P2P_accounting

# Create your views here.
def p2p_accounting(request):
    receipt_accting = P2P_accounting.objects.filter( accounting_entry='PO Receipt').filter(item_type='Expense')
    deliver_accting = P2P_accounting.objects.filter( accounting_entry='PO Deliver').filter(item_type='Expense')
    return render(request, 'p2p/p2p_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting})

def inv_accounting(request):
    receipt_accting = P2P_accounting.objects.filter( accounting_entry='PO Receipt').filter(item_type='Inventory')
    deliver_accting = P2P_accounting.objects.filter( accounting_entry='PO Deliver').filter(item_type='Inventory')
    return render(request, 'p2p/p2p_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting})
    return render(request,'p2p/p2p_accounting.html',{})