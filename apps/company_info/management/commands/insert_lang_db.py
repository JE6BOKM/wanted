# myapp/management/commands/insert_lang_db.py
from django.core.management.base import BaseCommand
from apps.company_info.models import Language

class Command(BaseCommand):     
    help = 'insert data to languages Table'     

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)

    def handle(self, *args, **options):
        name = options['name']
        language = Language(name=name)
        language.save()

        self.stdout.write('Successfully make language "%s"' % name)