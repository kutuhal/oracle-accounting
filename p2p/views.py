from django.shortcuts import render
from .models import P2P_accounting

# Create your views here.
def p2p_accounting(request):
    receipt_accting = P2P_accounting.objects.filter( accounting_entry='PO Receipt')
    deliver_accting = P2P_accounting.objects.filter( accounting_entry='PO Deliver')
    return render(request, 'p2p/p2p_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting})