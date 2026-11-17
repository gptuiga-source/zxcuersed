import os                                          # работа с переменными окружения
from pathlib import Path                           # удобные пути

from dotenv import load_dotenv                     # библиотека для чтения .env

BASE_DIR = Path(__file__).resolve().parent.parent  # корень проекта (две папки вверх)

load_dotenv(BASE_DIR / ".env")                     # читаем .env и кладём переменные в окружение

SECRET_KEY = os.getenv("SECRET_KEY")               # ключ для подписи сессий и CSRF
DEBUG = os.getenv("DEBUG", "True") == "True"       # True - режим разработки
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")  # список разрешённых хостов

INSTALLED_APPS = [                                 # список подключённых приложений
    "django.contrib.admin",                        # встроенная админка
    "django.contrib.auth",                         # встроенная авторизация
    "django.contrib.contenttypes",                 # типы контента (нужно для auth)
    "django.contrib.sessions",                     # сессии
    "django.contrib.messages",                     # всплывающие сообщения
    "django.contrib.staticfiles",                  # статика (css/js)
    'apps.accounts',
    'apps.catalog',
    'apps.journal.apps.JournalConfig',
]

MIDDLEWARE = [                                     # промежуточные слои между запросом и ответом
    "django.middleware.security.SecurityMiddleware",        # базовая безопасность
    "django.contrib.sessions.middleware.SessionMiddleware", # сессии
    "django.middleware.common.CommonMiddleware",            # общие правила
    "django.middleware.csrf.CsrfViewMiddleware",            # защита от CSRF
    "django.contrib.auth.middleware.AuthenticationMiddleware", # request.user
    "django.contrib.messages.middleware.MessageMiddleware",    # messages framework
]

ROOT_URLCONF = "priject.urls"                      # где лежит корневой urls.py

TEMPLATES = [                                      # настройки шаблонов
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # движок Django
        "DIRS": [BASE_DIR / "templates"],          # где искать общие шаблоны
        "APP_DIRS": True,                          # искать также в templates/ приложений
        "OPTIONS": {
            "context_processors": [                # переменные во всех шаблонах
                "django.template.context_processors.request",          # request
                "django.contrib.auth.context_processors.auth",         # user
                "django.contrib.messages.context_processors.messages", # messages
            ],
        },
    },
]

WSGI_APPLICATION = "priject.wsgi.application"     # точка входа для сервера
AUTH_USER_MODEL = 'accounts.User'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "ams"),
        "USER": os.getenv("POSTGRES_USER", "ams"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "ams"),
        "HOST": os.getenv("POSTGRES_HOST", "127.0.0.1"),
        "PORT": os.getenv("POSTGRES_PORT", "5434"),
    }
}

LANGUAGE_CODE = "ru-ru"                            # русский язык
TIME_ZONE = "Europe/Moscow"                        # московское время
USE_I18N = True                                    # включить переводы
USE_TZ = True                                      # хранить время с таймзоной

STATIC_URL = "static/"                             # URL для статики
MEDIA_URL = "media/"                               # URL для загруженных файлов
MEDIA_ROOT = BASE_DIR / "media"                    # папка для файлов

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField" # тип PK по умолчанию
