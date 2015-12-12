from django.shortcuts import render
from .models import P2P_accounting
from p2p.forms import P2PForm

# Create your views here.
def p2p_accounting(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = P2PForm(request.POST)
        if form.is_valid(): # All validation rules pass
            item_type_val = form.cleaned_data ['item_type']
            print(item_type_val )
        else:
            #this is fallback and usually not used since we are using 'Choices' in our form
            item_type_val ='Expense'
    else:
        #Initial load when the request != POST (e.g. GET)
        form=P2PForm()
        #setting item type to Expense
        item_type_val ='Expense'
    receipt_accting = P2P_accounting.objects.filter( accounting_entry='PO Receipt').filter(item_type=item_type_val)
    deliver_accting = P2P_accounting.objects.filter( accounting_entry='PO Deliver').filter(item_type=item_type_val)
    invoice_accting = P2P_accounting.objects.filter( accounting_entry='AP Invoice')
    payment_accting = P2P_accounting.objects.filter( accounting_entry='AP Payment')
    
    return render(request, 'p2p/p2p_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting,
        'ap_invoice_accting':invoice_accting, 'ap_payment_accting':payment_accting,
        'form': form})

def inv_accounting(request):
    receipt_accting = P2P_accounting.objects.filter( accounting_entry='PO Receipt').filter(item_type='Inventory')
    deliver_accting = P2P_accounting.objects.filter( accounting_entry='PO Deliver').filter(item_type='Inventory')
    invoice_accting = P2P_accounting.objects.filter( accounting_entry='AP Invoice')
    payment_accting = P2P_accounting.objects.filter( accounting_entry='AP Payment')
    return render(request, 'p2p/inv_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting,
        'ap_invoice_accting':invoice_accting, 'ap_payment_accting':payment_accting})