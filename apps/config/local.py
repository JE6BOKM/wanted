import os

from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    # django extensions
    INSTALLED_APPS += (
        # django extensions
        "django_extensions",
    )

    # Mail
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    REST_FRAMEWORK = Common.REST_FRAMEWORK
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = [  # noqa
        "apps.core.authentications.AutoLoginAuthentication",
    ]
