from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

# ✅ تسجيل مستخدم جديد
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "كلمتا المرور غير متطابقتين.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم بالفعل.")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user)  # إنشاء ملف شخصي افتراضي
        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
        return redirect("login")

    return render(request, "accounts-templates/register.html")


# ✅ تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح.")
            return redirect("home")  # غيّر المسار حسب اسم صفحتك الرئيسية
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")
            return redirect("login")

    return render(request, "accounts-templates/login.html")
