from typing import Any, Sequence

from django.conf import settings
from django.utils.timezone import now

import factory
from factory.django import DjangoModelFactory
from faker import Faker

__all__ = ["UserFactory"]

fake = Faker()


class UserFactory(DjangoModelFactory):
    username = factory.Sequence(lambda n: fake.user_name() + f"{n}")
    email = factory.Faker("email")
    date_joined = factory.LazyAttribute(lambda x: now())

    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ["email"]

    # without the below LOC, password is not hashed and we cannot login
    @factory.post_generation
    def password(self, _: bool, extracted: Sequence[Any], **kwargs):
        password = extracted if extracted else "my_password"
        self.set_password(password)
