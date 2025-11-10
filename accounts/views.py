from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

# ✅ إنشاء حساب جديد
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # 🧩 تحقق من تطابق كلمة المرور
        if password != confirm_password:
            messages.error(request, "كلمتا المرور غير متطابقتين.")
            return redirect("accounts:register")

        # 🧩 تحقق من وجود المستخدم مسبقاً
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم بالفعل.")
            return redirect("accounts:register")

        # 🧩 إنشاء مستخدم جديد وملف شخصي افتراضي
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user)
        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
        return redirect("accounts:login")

    return render(request, "accounts-templates/register.html")


# ✅ تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # تحقق من بيانات الدخول
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"مرحبًا {user.username}! تم تسجيل الدخول بنجاح.")
            # ✅ التوجيه إلى الصفحة الرئيسية للتطبيق (catalog)
            return redirect("catalog:home")
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")
            return redirect("accounts:login")

    return render(request, "accounts-templates/login.html")
