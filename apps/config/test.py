"""
With these settings, tests run faster.
"""

import os

from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Test(Common):
    # GENERAL
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    SECRET_KEY = os.getenv(
        "DJANGO_SECRET_KEY",
        default="V3S2aT1P0MN9WOZSEUEsVZiomVOWubAoxnMIn61oDzv4hSAjzfNiwIcqprAuI8qw",
    )
    # https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
    TEST_RUNNER = "django.test.runner.DiscoverRunner"

    # CACHES
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#caches
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "",
        }
    }

    # PASSWORDS
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
    PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

    # TEMPLATES
    # ------------------------------------------------------------------------------
    TEMPLATES = Common.TEMPLATES
    TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
        (
            "django.template.loaders.cached.Loader",
            [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        )
    ]

    # EMAIL
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
    EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

    REST_FRAMEWORK = Common.REST_FRAMEWORK
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = [  # noqa
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ]
