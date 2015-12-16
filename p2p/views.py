from django.shortcuts import render
from .models import P2P_accounting
from p2p.forms import P2PForm, O2CForm

# Create your views here.
def p2p_accounting(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = P2PForm(request.POST)
        if form.is_valid(): # All validation rules pass
            item_type_val = form.cleaned_data ['item_type']

            period_end_accrual_val = form.cleaned_data ['period_end_accrual']
            allow_recon_accounting = form.cleaned_data ['allow_recon_accounting']
            print(period_end_accrual_val    )
        else:
            #this is fallback and usually not used since we are using 'Choices' in our form
            item_type_val ='Expense'
            allow_recon_accounting = False
    else:
        #Initial load when the request != POST (e.g. GET)
        form=P2PForm()
        #setting form variables to default values for a != POST (e.g. GET request)
        item_type_val ='Expense'
        period_end_accrual_val =False
        allow_recon_accounting = False
    receipt_accting = P2P_accounting.objects.filter( 
            accounting_entry='PO Receipt').filter(item_type=item_type_val).filter (period_end_accrual=period_end_accrual_val)
    deliver_accting = P2P_accounting.objects.filter( 
        accounting_entry='PO Deliver').filter(item_type=item_type_val)
    invoice_accting = P2P_accounting.objects.filter( accounting_entry='AP Invoice').filter(period_end_accrual=period_end_accrual_val)
    payment_accting = P2P_accounting.objects.filter( accounting_entry='AP Payment').filter(allow_recon_accounting=allow_recon_accounting)
    recon_accting = P2P_accounting.objects.filter( accounting_entry='AP Payment Reco').filter(allow_recon_accounting=allow_recon_accounting)
    
    return render(request, 'p2p/p2p_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting,
        'ap_invoice_accting':invoice_accting, 'ap_payment_accting':payment_accting,'ap_payment_recon_accting': recon_accting,
        'form': form})

def o2c_accounting(request):
    form=O2CForm()
    return render(request, 'p2p/o2c_accounting.html',{'form': form})
