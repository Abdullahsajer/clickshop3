from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.conf import settings

# 📁 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 مفتاح التشفير
SECRET_KEY = 'django-insecure-mwrbq76gclmb8ykb=70@3^0*-e-d(!wxgc17&7bfsp1+86g3&y'

# ⚙️ وضع التطوير
DEBUG = True

# 🌐 العناوين المسموح بها
ALLOWED_HOSTS = []

# 📦 التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ تطبيقات المشروع
    'accounts.apps.AccountsConfig',
    'catalog.apps.CatalogConfig',
    'sales.apps.SalesConfig',

    # ☁️ إضافة تطبيق Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# 🧱 الوسائط الوسطية
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

# 🧾 إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

# 🗄️ قاعدة البيانات
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

# 🌍 اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# 🖼️ إعداد الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ☁️ إعداد Cloudinary كخدمة تخزين للوسائط
cloudinary.config(
    cloud_name="dkjrjd6jc",
    api_key="331143126546926",
    api_secret="xJcHaqSS3qM2UCVrS6_68cEKZd8"
)

# 🖼️ إعداد ملفات الوسائط باستخدام Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# 🆔 تعريف تلقائي للأعمدة
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
