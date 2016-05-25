from django.shortcuts import render
from .models import Product, Product_bottom, Product_top


#product_list
def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'product/product_list.html', {
    'product_list':product_list})

def product_top_list(request):
    product_list = Product_top.objects.all()
    return render(request, 'product/product_top_list.html', {
    'product_list':product_list})

def product_bottom_list(request):
    product_list = Product_bottom.objects.all()
    return render(request, 'product/product_bottom_list.html', {
    'product_list':product_list})



#product_detail
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product/product_detail.html', {
        'product':product,

        })
def product_top_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product/product_detail.html', {
        'product':product,

        })

def product_bottom_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product/product_detail.html', {
        'product':product,

        })

def get_products(request, next_pk):
    '''return the products from pk to pk+100'''
    nid = int(next_pk)
    products = Product.objects.order_by('-pk')[nid:nid+3]
    if request.is_ajax():
        return render(request, 'product/product.ajax.html', {'next_pk': nid+3, 'products': products})
    else:
        return render(request, 'product/view_products.html', {'next_pk': nid+3, 'products': products})

# Create your views here.
