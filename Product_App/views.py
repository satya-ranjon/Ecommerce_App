from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# import 
from django.views.generic import ListView,DetailView
# import models 
from .models import Products
# Create your views here.

def Shop(request):
    Product_list = Products.objects.all()
    if request.method == 'GET':
        search = request.GET.get('search','')
        result = Products.objects.filter(name__icontains = search)
        print(result)
    print(Product_list)
    return render(request,'Product_App/shop.html',{'Product_list':Product_list,'result':result,'search':search})


# class Home(ListView):
#     model = Products
#     context_object_name = 'Product_list'
#     template_name='Product_App/shop.html'
    
class ProductDitels(DetailView,LoginRequiredMixin):
    model = Products
    context_object_name = 'Product_detiels'
    template_name='Product_App/product_detiels.html'