# myapp/management/commands/insert_lang_db.py
from django.core.management.base import BaseCommand
from apps.company_info.models import Tag

class Command(BaseCommand):     
    help = 'insert data to tags table'     

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('language_id', type=int)

    def handle(self, *args, **options):
        name = options['name']
        language_id = options['language_id']
        tag = Tag(name=name, language_id=language_id)
        tag.save()

        self.stdout.write('Successfully make tag "%s"' % name)