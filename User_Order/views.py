from django.db import models
from django.shortcuts import render,get_object_or_404,redirect
# Authentications
from django.contrib.auth.decorators import login_required
# models
from .models import Oreder,Cart
from Product_App.models import Products
# messages
from django.contrib import messages


# Create your views here.


@login_required()
def Add_to_cart(request,pk):
    item = get_object_or_404(Products, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Oreder.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request,'This item quantity was updated. ')
            return redirect('shop')
        else:
            order.orderitems.add(order_item[0])
            messages.info(request,'This item was added to your cart.')
            return redirect('shop')
    else:
        order = Oreder(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request,'This item was added to your cart!')
        return redirect('shop')


@login_required()
def Cart_Views (request):
    carts = Cart.objects.filter(user=request.user, purchased=False )
    orders = Oreder.objects.filter(user=request.user,ordered=False)
    if carts.exists() and orders.exists():
        orders = orders[0]
        return render(request,'User_Order/card.html',{'carts':carts,'order':orders})
    else:
        messages.warning(request,"You don'i have any item in your cart" )
        return redirect('shop')
    
    

@login_required()
def Remove_Card_Item(request,pk):
    item = get_object_or_404(Products, pk=pk)
    order_qs = Oreder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request,'This item was removed form your cart')
            return redirect('card')
        else:
            messages.info(request,'This item was not in your cart')
            return redirect('shop')
    else:
        messages.info(request,"You don't have an active order")
        return redirect('shop')



@login_required()
def Increase_Card(request,pk):
    item = get_object_or_404(Products, pk=pk)
    order_qs = Oreder.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request,f"{item.name} quantity has been update ")
                return redirect('card')
        else:
            messages.info(request, f"{item.name} is not in your Cart")
    else:
        messages.info(request,"You don't have an active order")
        return redirect('shop')
    



@login_required()
def Decrese_Cart(request,pk):
    item = get_object_or_404(Products,pk=pk)
    order_qs = Oreder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request,f"{item.name} quantity has been update ")
                return redirect('card')
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request,f"{item.name} quantity has been update ")
                return redirect('card')
        else:
            messages.info(request,f"{item.name}You don't have an your cart")
            return redirect('shop')
    else:
        messages.info(request, "You don't have an active order")
        return redirect('shop')
    
        