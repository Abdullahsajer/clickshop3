from django.contrib import admin
from .models import Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):  # يمكن أيضاً استخدام StackedInline
    model = ProductImage
    extra = 1  # عدد الحقول الفارغة المضافة افتراضياً
    verbose_name = "صورة المنتج"
    verbose_name_plural = "صور المنتج"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]  # ✅ دمج الصور هنا داخل صفحة المنتج


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# لإزالة ظهور صور المنتجات بشكل مستقل في القائمة الجانبية:
# admin.site.unregister(ProductImage)