from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import Cart, CartItem, Order, OrderItem


# ✅ دالة مساعدة لإرجاع عدد المنتجات في السلة (تُستخدم في كل الصفحات)
def get_cart_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        return cart.items.count() if cart else 0
    return 0


# 🛒 عرض السلة
@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    # 🧮 حساب الإجماليات
    cart_data = []
    total_price = 0
    for item in items:
        item_total = item.product.price * item.quantity
        total_price += item_total
        cart_data.append({
            'id': item.id,
            'name': item.product.name,
            'price': item.product.price,
            'quantity': item.quantity,
            'item_total': item_total,
        })

    # ✅ عدد العناصر في السلة (يُستخدم في الهيدر)
    cart_count = get_cart_count(request)

    context = {
        'cart': cart,
        'cart_items': cart_data,
        'total_price': total_price,
        'cart_count': cart_count,
    }
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


# ❌ حذف منتج من السلة
@login_required
def remove_from_cart(request, item_id):
    try:
        item = CartItem.objects.get(id=item_id, cart__user=request.user)
        item.delete()
        messages.success(request, "🗑️ تم حذف المنتج من السلة بنجاح.")
    except CartItem.DoesNotExist:
        messages.error(request, "⚠️ المنتج غير موجود في السلة.")
    return redirect('sales:cart')


# 🔄 تحديث كمية المنتج في السلة
@login_required
def update_cart_item(request, item_id):
    if request.method == 'POST':
        new_quantity = request.POST.get('quantity')
        try:
            item = CartItem.objects.get(id=item_id, cart__user=request.user)
            if new_quantity.isdigit() and int(new_quantity) > 0:
                item.quantity = int(new_quantity)
                item.save()
                messages.success(request, "✅ تم تحديث الكمية بنجاح.")
            else:
                messages.warning(request, "⚠️ الكمية يجب أن تكون رقمًا موجبًا.")
        except CartItem.DoesNotExist:
            messages.error(request, "❌ لم يتم العثور على المنتج.")
    return redirect('sales:cart')


# 💳 إتمام الطلب
@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    # ✅ عدد العناصر في السلة (للهيدر)
    cart_count = get_cart_count(request)

    if request.method == 'POST':
        address = request.POST.get('address', '')
        total = sum(item.product.price * item.quantity for item in items)

        order = Order.objects.create(
            user=request.user,
            address=address,
            total=total,
        )

        for item in items:
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

    context = {
        'cart': cart,
        'cart_count': cart_count,
    }
    return render(request, 'sales-templates/checkout.html', context)


# 📜 عرض الطلبات السابقة
@login_required
def my_orders_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # ✅ عدد العناصر في السلة (للهيدر)
    cart_count = get_cart_count(request)

    context = {
        'orders': orders,
        'cart_count': cart_count,
    }
    return render(request, 'sales-templates/my_orders.html', context)


# 📦 عرض تفاصيل الطلب
@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # ✅ عدد العناصر في السلة (للهيدر)
    cart_count = get_cart_count(request)

    context = {
        'order': order,
        'cart_count': cart_count,
    }
    return render(request, 'sales-templates/order_detail.html', context)
