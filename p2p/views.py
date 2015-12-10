from django.shortcuts import render
from .models import P2P_accounting

# Create your views here.
def p2p_accounting(request):
    accounting = P2P_accounting.objects.all()
    return render(request, 'p2p/p2p_accounting.html',{'p2p_accounting': accounting })