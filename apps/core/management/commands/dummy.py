from math import ceil

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

import pandas as pd
from django_extensions.management.shells import import_objects

from test.factories import (
    CompanyFactory,
    CompanyNameFactory,
    LanguageFactory,
    TagFactory,
    UserFactory,
)

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

        # company info dummy data
        data = pd.read_csv("wanted_temp_data.csv")

        for row in data.iloc:
            index, values = row.index, row.values
            company_model = CompanyFactory()
            for i in range(len(index)):
                model, lang = index[i].split("_")
                language_model = LanguageFactory(name=lang)
                if values[i] != "nan" and model == "company":
                    CompanyNameFactory(
                        name=values[i], c_id=company_model, language=language_model
                    )
                elif values[i] != "nan" and model == "tag":
                    tags = values[i].split("|")
                    for tag in tags:
                        t = TagFactory(name=tag, language=language_model)
                        company_model.tags.add(t)

        self.stdout.write("Finish load dummy")
