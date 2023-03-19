from django.shortcuts import render, redirect
from .forms import ProductAddForm, CategoryAddForm
from .models import Category, Product
from django.contrib.auth.models import User

# Create your views here.

# dashboard
def dashboard_index(request):
    return render(request, 'dashboard/dashboard.html')

# categories
def category_add(request):
    form = CategoryAddForm()
    context = {"form": form}

    if request.method == "POST":
        catgry = Category()
        catgry.category_name = request.POST.get('category_name')
        catgry.save()

    return render(request, 'categories/add_category.html', context)

# products
def product_add(request):
    add_product = ProductAddForm()
    context = {"form": add_product}

    if request.method == "POST":
        category = Category.objects.get(id=request.POST.get('category'))
        user = User.objects.get(username='puppet')

        product = Product()
        product.title = request.POST.get('title')
        product.desc = request.POST.get('desc')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.discount = request.POST.get('discount')
        product.cod = request.POST.get('cod')
        product.category = category
        product.user = user
        product.save()
        return redirect('list-product')
    return render(request, 'products/product_add.html', context)

def product_index(request):
    return render(request, 'products/product_index.html')