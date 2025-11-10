from pathlib import Path

# 📁 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 مفتاح التشفير (يجب تغييره في بيئات الإنتاج)
SECRET_KEY = 'django-insecure-mwrbq76gclmb8ykb=70@3^0*-e-d(!wxgc17&7bfsp1+86g3&y'

# ⚙️ وضع التطوير
DEBUG = True

# 🌐 العناوين المسموح بها
ALLOWED_HOSTS = []


# 📦 التطبيقات المثبتة
INSTALLED_APPS = [
    # 🧩 تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ تطبيقات المشروع المخصصة
    'accounts.apps.AccountsConfig',  # إدارة الحسابات والمستخدمين
    'catalog.apps.CatalogConfig',    # إدارة المنتجات والتصنيفات
    'sales.apps.SalesConfig',        # إدارة الطلبات والسلة
]


# 🧱 الوسائط الوسطية (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 📍 ملف URLs الجذري
ROOT_URLCONF = 'clickshop3.urls'


# 🧾 إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # ✅ تعريف مجلد القوالب العام داخل المشروع
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# 🧩 إعداد WSGI
WSGI_APPLICATION = 'clickshop3.wsgi.application'


# 🗄️ إعداد قاعدة البيانات (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔐 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🌍 إعداد اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True


# 🖼️ إعداد الملفات الثابتة (Static Files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # مجلد الملفات الثابتة أثناء التطوير
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # مجلد تجميع الملفات الثابتة عند النشر


# 🖼️ إعداد ملفات الوسائط (Media)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# 🆔 تعريف تلقائي للأعمدة في النماذج
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
