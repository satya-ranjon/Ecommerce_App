from django.contrib.auth import login
from django.core.checks import messages
from django.urls import reverse
from django.shortcuts import redirect, render,HttpResponseRedirect

# models and form 
from User_Order.models import Cart, Oreder
from .models import BillingAddress
from .forms import BillingForm

# 
from django.contrib.auth.decorators import login_required
# messages 
from django.contrib import messages

#for payment 
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt
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




@login_required()
def Payment(request):
    saved_address =BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_filled():
        messages.info(request,f"Please complate profile details!")
        return redirect("chackout")
    
    if not request.user.profile.is_fully_filled():
        messages.info(request,f"Please complate profile details!")
        return redirect('user_ch_pro')
    
    store_id = 'dk6193ca5d2962f'
    api_key = 'dk6193ca5d2962f@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=api_key)
    
    status_url = request.build_absolute_uri(reverse('py_com'))
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)

    order_qs = Oreder.objects.filter(user=request.user, ordered=False)
    order_item = order_qs[0].orderitems.all()
    order_item_count = order_qs[0].orderitems.count()
    order_total = order_qs[0].get_total()
    
    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='Mix', product_name=order_item, num_of_item=order_item_count, shipping_method='Courier', product_profile='None')

    current_user = request.user
    

    mypayment.set_customer_info(name=current_user.profile.full_name, email=current_user.email, address1=current_user.profile.address_1, address2=current_user.profile.address_1, city=current_user.profile.city, postcode=current_user.profile.zipcode, country=current_user.profile.country, phone=current_user.profile.country)

    
    mypayment.set_shipping_info(shipping_to=current_user.profile.full_name, address=saved_address.address, city=saved_address.city, postcode=saved_address.zipcode, country=saved_address.country)

    response_data = mypayment.init_payment()
    print(response_data)


    return redirect(response_data['GatewayPageURL'])




@csrf_exempt
def Complate(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']

        bank_tran_id = payment_data['bank_tran_id']
    
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request,f"Your Payment Complated! Page will be redirect after 5 secound !")
            
            return HttpResponseRedirect(reverse('purched', kwargs={'val_id':val_id, 'tran_id':tran_id},))
        
        elif status == 'FAILED':
            messages.warning(request,f"Your Payment Fild Please Try Agin!  Page will be redirect after 5 secound !")
        
    return render(request,'Payment_App/py_com.html',{})



@login_required()
def Purched(request,val_id,tran_id):
    order_qs = Oreder.objects.filter(user=request.user, ordered = False)
    order = order_qs[0]
    order.ordered = True
    order.orderId = tran_id
    order.paymentId = val_id
    order.save()
    cart_items = Cart.objects.filter(user=request.user, purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()
    return HttpResponseRedirect(reverse('py_com'))


@login_required
def order_view_his(request):
    try:
        orders = Oreder.objects.filter(user=request.user, ordered=True)
        context = {"orders": orders}
    except:
        messages.warning(request, "You do no have an active order")
        return redirect("shop")
    return render(request, "Payment_App/order_history.html", context)