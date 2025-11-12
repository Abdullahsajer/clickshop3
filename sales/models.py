from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="المستخدم")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "سلة"
        verbose_name_plural = "السلات"

    def __str__(self):
        return f"سلة {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name="السلة")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    class Meta:
        verbose_name = "عنصر سلة"
        verbose_name_plural = "عناصر السلة"

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'جديد'),
        ('paid', 'تم الدفع'),
        ('shipped', 'تم الشحن'),
        ('delivered', 'تم التوصيل'),
        ('cancelled', 'ملغي'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    address = models.CharField(max_length=500, verbose_name="عنوان الشحن")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="إجمالي المبلغ")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="الحالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="الطلب")
    product = models.CharField(max_length=200, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.quantity} × {self.product}"

    # ✅ دالة لحساب الإجمالي الكلي للسلة
    @property
    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())
