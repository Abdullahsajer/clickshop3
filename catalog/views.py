from django.shortcuts import render
from .models import Product


# 🏠 الصفحة الرئيسية (تظهر البنر + المنتجات)
def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# 🛍️ صفحة المنتجات المستقلة (قائمة المنتجات فقط)
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'catalog-templates/product_list.html', {'products': products})
