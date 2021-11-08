from math import ceil

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from django_extensions.management.shells import import_objects

from test.factories import UserFactory

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "-c",
            type=str,
            help="Add number of posts",
        )

    def handle(self, *args, **kwargs):
        if not kwargs.get("c"):
            posts_cnt = 10
        else:
            posts_cnt = int(kwargs.get("p"))

        self.stdout.write("Start loading dummy")

        # populates globals() with django models, so no need to worry about importing them
        # https://stackoverflow.com/questions/59267620/how-to-import-all-django-models-and-more-in-a-script
        options = {"quiet_load": True}
        style = BaseCommand().style

        imported_objects = import_objects(options, style)
        globals().update(imported_objects)

        UserFactory.create_batch(size=ceil(posts_cnt / 10))

        self.stdout.write("Finish load dummy")
