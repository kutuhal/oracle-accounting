from django import forms
from p2p.models import P2P_accounting
from django.forms import ModelForm, Select

class P2PForm(forms.ModelForm):

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = P2P_accounting
        fields = ['item_type','period_end_accrual', 'allow_recon_accounting']
    # For adding CSS class to the fields
    def __init__(self, *args, **kwargs):
        super(P2PForm, self).__init__(*args, **kwargs)
        self.fields['item_type'].widget.attrs['class'] = 'form-control'
        self.fields['period_end_accrual'].widget.attrs['class'] = 'form-control'
        self.fields['allow_recon_accounting'].widget.attrs['class'] = 'form-control'

class O2CForm(forms.ModelForm):

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = P2P_accounting
        fields = ['oe_line_flow']