from django.shortcuts import render
from .models import P2P_accounting
from p2p.forms import P2PForm, O2CForm
from django.db.models import Q

ITEM_TYPES = ( ('Expense','Expense'), ('Inventory','Inventory'))
ACCRUE_EXP_ITEMS = (('At Receipt', 'At Receipt'), ('Period End','Period End'))

# Create your views here.
def p2p_accounting(request):
    #Initial load when the request != POST (e.g. GET)
    form=P2PForm()
    #setting form variables to default values for a != POST (e.g. GET request)
    item_type_val ='Expense'
    period_end_accrual_val ='At Receipt'
    allow_recon_accounting = False
    form.fields['item_type'].choices = ITEM_TYPES # Limiting choices at GET
    form.fields['period_end_accrual'].choices = ACCRUE_EXP_ITEMS  # Limiting choices at GET

    # A HTTP POST?
    if request.method == 'POST':
        form = P2PForm(request.POST)
        form.fields['item_type'].choices = ITEM_TYPES # Limiting choices after POST request of form
        form.fields['period_end_accrual'].choices = ACCRUE_EXP_ITEMS  # Limiting choices at GET
        if form.is_valid(): # All validation rules pass

            item_type_val = form.cleaned_data ['item_type']
            print ('Item type is'+ item_type_val)
            period_end_accrual_val = form.cleaned_data ['period_end_accrual']
            allow_recon_accounting = form.cleaned_data ['allow_recon_accounting']
            print(period_end_accrual_val    )
        else:
            #this is fallback and usually not used since we are using 'Choices' in our form
            item_type_val ='Expense'
            allow_recon_accounting = False
            period_end_accrual_val ='At Receipt'

    receipt_accting = P2P_accounting.objects.filter( 
            accounting_entry='PO Receipt').filter(item_type=item_type_val).filter (period_end_accrual=period_end_accrual_val)
    deliver_accting = P2P_accounting.objects.filter( 
        accounting_entry='PO Deliver').filter(item_type=item_type_val)
    # Invoice Accounting using Complex lookups with Q objects
    invoice_accting = P2P_accounting.objects.filter(
        Q(accounting_entry='AP Invoice'), Q(item_type=item_type_val ) | Q(item_type='Not Relevant' ),
        (Q(period_end_accrual=period_end_accrual_val) | Q(period_end_accrual='Not Relevant'))
        )
    payment_accting = P2P_accounting.objects.filter( accounting_entry='AP Payment').filter(allow_recon_accounting=allow_recon_accounting)
    recon_accting = P2P_accounting.objects.filter( accounting_entry='AP Payment Reco').filter(allow_recon_accounting=allow_recon_accounting)
    pe_accrual_accting = P2P_accounting.objects.filter( 
            accounting_entry='PO Receipt Accruals - Period End').filter(item_type=item_type_val).filter (period_end_accrual=period_end_accrual_val)
    return render(request, 'p2p/p2p_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting,
        'ap_invoice_accting':invoice_accting, 'ap_payment_accting':payment_accting,'ap_payment_recon_accting': recon_accting,
        'po_pe_accrual_accting': pe_accrual_accting,
        'form': form})

def o2c_accounting(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = O2CForm(request.POST)
        if form.is_valid(): # All validation rules pass
            oe_line_flow_val = form.cleaned_data ['oe_line_flow']

    
    else:
        #Initial load when the request != POST (e.g. GET)
        form=O2CForm() 
        #setting form variables to default values for a != POST (e.g. GET request)
        oe_line_flow_val = 'Bill Only'
    #filtering the accounting entries
    pick_confirm_accting = P2P_accounting.objects.filter( accounting_entry='Pick Confirm'). filter(oe_line_flow= oe_line_flow_val)
    ship_confirm_accting = P2P_accounting.objects.filter( accounting_entry='Ship Confirm'). filter(oe_line_flow= oe_line_flow_val)
    ar_revenue_recog_accting = P2P_accounting.objects.filter( accounting_entry='Revenue Recognition')
    ar_invoice_accting = P2P_accounting.objects.filter( accounting_entry='AR Invoice')
    std_receipt_accting = P2P_accounting.objects.filter( 
            accounting_entry='AR Receipt')
    ar_recon_accting = P2P_accounting.objects.filter( accounting_entry='AR Receipt Recon')
    return render(request, 'p2p/o2c_accounting.html',
        {'oe_pick_confirm_accting':pick_confirm_accting , 'oe_ship_confirm_accting': ship_confirm_accting, 
        'ar_revenue_recog_accting': ar_revenue_recog_accting,
        'ar_invoice_accting':ar_invoice_accting, 'ar_receipt_accting': std_receipt_accting, 
        'ar_receipt_recon_accting': ar_recon_accting, 
        'form': form})
