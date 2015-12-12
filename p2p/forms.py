from django import forms
from p2p.models import P2P_accounting
from django.forms import ModelForm, Select

class P2PForm(forms.ModelForm):

    # An inline class to provide additional information on the form.
    class Meta:
        ITEM_TYPES = ( ('Expense','Expense'), ('Inventory','Inventory'))    
        # Provide an association between the ModelForm and a model
        model = P2P_accounting
        fields = ['item_type','period_end_accrual']
        widgets = {
            'item_type':  Select(choices= ITEM_TYPES),
        }