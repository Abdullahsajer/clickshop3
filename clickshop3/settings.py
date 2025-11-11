from pathlib import Path
import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url

# 📁 تحميل متغيرات البيئة
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# 🔐 إعدادات الأمان
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-key-in-production")
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "clickshop3.onrender.com,127.0.0.1,localhost"
).split(",")

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

    # ☁️ تطبيق Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# 🧱 الوسائط الوسطية (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ✅ دعم الملفات الثابتة في الإنتاج
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 📍 ملف URLs الجذري
ROOT_URLCONF = 'clickshop3.urls'

# 🧾 إعداد القوالب (Templates)
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

# 🗄️ إعداد قاعدة البيانات (SQLite محلياً - PostgreSQL على Render)
if DEBUG:
    # قاعدة البيانات المحلية (تطوير)
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("DEV_DB_ENGINE", "django.db.backends.sqlite3"),
            'NAME': BASE_DIR / os.getenv("DEV_DB_NAME", "db.sqlite3"),
        }
    }
else:
    # قاعدة البيانات في بيئة الإنتاج (Render)
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True
        )
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

# 🖼️ إعداد الملفات الثابتة (Static files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ✅ تفعيل WhiteNoise لتقديم الملفات الثابتة في Render
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ☁️ إعداد Cloudinary للوسائط (Media)
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("CLOUD_API_KEY"),
    api_secret=os.getenv("CLOUD_API_SECRET"),
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🆔 تعريف تلقائي للأعمدة
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🧠 نظام تسجيل الأخطاء (Logging)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'errors.log',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['file', 'console'],
        'level': 'ERROR',
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
