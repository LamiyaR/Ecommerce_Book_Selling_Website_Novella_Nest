from pathlib import Path
import os

# Optional: load .env locally if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# If dj_database_url is available, we'll use it; otherwise we'll fallback to SQLite
try:
    import dj_database_url
except Exception:
    dj_database_url = None

# --------------------------------------------------------------------------------------
# Base paths
# --------------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------------------
# Security / Env
# --------------------------------------------------------------------------------------
# DO NOT commit real secrets. In Render or your host, set these env vars.
SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-not-secure")
DEBUG = os.getenv("DEBUG", "True") == "True"

# Comma-separated lists in env, e.g.:
# ALLOWED_HOSTS=localhost,127.0.0.1,your-service.onrender.com
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Comma-separated full origins for CSRF (https URLs), e.g.:
# CSRF_TRUSTED_ORIGINS=https://your-service.onrender.com
CSRF_TRUSTED_ORIGINS = (
    os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if os.getenv("CSRF_TRUSTED_ORIGINS")
    else []
)

# --------------------------------------------------------------------------------------
# Apps
# --------------------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "store",
]

# --------------------------------------------------------------------------------------
# Middleware (WhiteNoise added for static files in production)
# --------------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # <-- add this
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bookshop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store.context_preprocessors.store_menu",
                "store.context_preprocessors.cart_menu",
            ],
        },
    },
]

WSGI_APPLICATION = "bookshop.wsgi.application"

# --------------------------------------------------------------------------------------
# Database: Use DATABASE_URL if present (Render/Heroku/etc), else SQLite
# --------------------------------------------------------------------------------------
if dj_database_url and os.getenv("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600, ssl_require=False)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# --------------------------------------------------------------------------------------
# Password validation
# --------------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------------------------------------------
# Internationalization
# --------------------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --------------------------------------------------------------------------------------
# Static & Media
# --------------------------------------------------------------------------------------
STATIC_URL = "/static/"

# Where collectstatic puts files (used by WhiteNoise/production)
STATIC_ROOT = BASE_DIR / "staticfiles"

# Optional additional static sources (only if this folder exists)
bookshop_static = BASE_DIR / "bookshop" / "static"
STATICFILES_DIRS = [bookshop_static] if bookshop_static.exists() else []

# Tell WhiteNoise to compress & hash static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media uploads (for local/dev). For production, consider S3/Cloudinary.
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --------------------------------------------------------------------------------------
# Email (console in dev)
# --------------------------------------------------------------------------------------
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend"
)

# --------------------------------------------------------------------------------------
# Security hardening toggles – safe defaults for production
# --------------------------------------------------------------------------------------
if not DEBUG:
    SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "True") == "True"
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Enable HSTS if you have HTTPS set up
    SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "31536000"))  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
