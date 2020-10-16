from django.shortcuts import render,get_object_or_404, redirect
from .models import Product
from .forms import AddProductForm

def products_list(request):
    products=Product.objects.all()
    return render(request, 'products/products-list.html',{'products':products})


def product_details(request, pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,'products/product-details.html', {'product':product})



def product_add(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return render(request, 'products/product-add-successful.html')

        else:
            form = AddProductForm()
    
        return render(request, 'products/product-add.html', {'form' : form})
    else:
        return redirect('products_list')

def product_edit(request, pk):
    if request.user.is_authenticated and  request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
           form = AddProductForm(request.POST,request.FILES, instance=product)
           if form.is_valid():
              form.save()
              return render(request,'products/product-add-successful.html')
        else:
            form = AddProductForm(instance=product)
        return render(request, 'products/product-add.html', {'form' : form})
    else:
        return redirect('products_list')

        
def product_delete(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('products_list')
    else:
        return redirect('products_list')