from django.contrib.auth import login
from django.core.checks import messages
from django.shortcuts import redirect, render,HttpResponseRedirect

# models and form 
from User_Order.models import Oreder
from .models import BillingAddress
from .forms import BillingForm

# 
from django.contrib.auth.decorators import login_required
# messages 
from django.contrib import messages

# Create your views here.

@login_required()
def ChackOut(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request,f"Shipping Address Saved!")
            return redirect('chackout')
    order_qs = Oreder.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_total()

    return render(request,'Payment_App/chackout.html',{'form':form,'order_items':order_items,'order_total':order_total,'saved_address':saved_address, })