from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import Cart, CartItem, Order, OrderItem


# 🛒 عرض السلة
@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {'cart': cart}
    return render(request, 'sales-templates/cart.html', context)


# ➕ إضافة منتج إلى السلة
@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'المنتج غير موجود.'})

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        return JsonResponse({'status': 'success', 'message': f'✅ تمت إضافة {product.name} إلى السلة!'})
    return JsonResponse({'status': 'error', 'message': 'طلب غير صالح'})


# 💳 إتمام الطلب
@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        address = request.POST.get('address', '')
        total = sum(item.product.price * item.quantity for item in cart.items.all())

        order = Order.objects.create(
            user=request.user,
            address=address,
            total=total,
        )

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product.name,
                price=item.product.price,
                quantity=item.quantity
            )

        # 🧹 تفريغ السلة بعد الطلب
        cart.items.all().delete()
        messages.success(request, "✅ تم إتمام الطلب بنجاح!")
        return redirect('sales:my_orders')

    context = {'cart': cart}
    return render(request, 'sales-templates/checkout.html', context)


# 📜 عرض الطلبات السابقة (تشمل جميع الحالات)
@login_required
def my_orders_view(request):
    # نجلب جميع الطلبات للعميل بدون فلترة على الحالة
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'sales-templates/my_orders.html', context)



# 📦 عرض تفاصيل الطلب
@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'order': order}
    return render(request, 'sales-templates/order_detail.html', context)
