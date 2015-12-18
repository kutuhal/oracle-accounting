from django import forms
from p2p.models import P2P_accounting
from django.forms import ModelForm, Select

class P2PForm(forms.ModelForm):

    # An inline class to provide additional information on the form.
    class Meta:
        
        # Provide an association between the ModelForm and a model
        model = P2P_accounting
        fields = ['item_type','period_end_accrual', 'allow_recon_accounting']

class O2CForm(forms.ModelForm):

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = P2P_accounting
        fields = ['oe_line_flow']