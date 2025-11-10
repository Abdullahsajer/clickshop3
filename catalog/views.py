from django.shortcuts import render

# 🏠 عرض الصفحة الرئيسية
def home_view(request):
    return render(request, 'home.html')
