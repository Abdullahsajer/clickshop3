from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ⚙️ تخصيص واجهة لوحة التحكم
admin.site.site_header = "لوحة التحكم - متجر كليك شوب"
admin.site.site_title = "لوحة التحكم"
admin.site.index_title = "مرحبًا بك في لوحة إدارة متجر كليك شوب"

urlpatterns = [
    # 🧭 لوحة التحكم
    path('admin/', admin.site.urls),

    # 🏠 جعل الكاتالوج هو الصفحة الرئيسية للموقع
    path('', include('catalog.urls')),

    # 👥 تطبيق الحسابات والمستخدمين
    path('accounts/', include('accounts.urls')),

    # 🛒 تطبيق السلة والطلبات
    path('sales/', include('sales.urls')),
]

# ✅ عرض ملفات الوسائط (media) والملفات الثابتة (static) أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
