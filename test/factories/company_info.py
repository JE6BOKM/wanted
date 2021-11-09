import factory
from factory.django import DjangoModelFactory
from faker import Faker

from apps.company_info.models import Company, CompanyName, Language, Tag

__all__ = [
    "LanguageFactory",
    "TagFactory",
    "CompanyFactory",
    "CompanyNameFactory",
    "CompanyNameFactory",
]

fake = Faker()


class LanguageFactory(DjangoModelFactory):
    name = factory.Faker("language_name")

    class Meta:
        model = Language
        django_get_or_create = ["name"]


class TagFactory(DjangoModelFactory):
    name = factory.Faker("word")
    language = factory.SubFactory(LanguageFactory)

    class Meta:
        model = Tag
        django_get_or_create = ["name"]


class CompanyFactory(DjangoModelFactory):
    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for tag in extracted:
                self.tags.add(tag)

    class Meta:
        model = Company


class CompanyNameFactory(DjangoModelFactory):
    name = factory.Faker("word")
    language = factory.SubFactory(LanguageFactory)
    c_id = factory.SubFactory(CompanyFactory)

    class Meta:
        model = CompanyName
        django_get_or_create = ["name"]
