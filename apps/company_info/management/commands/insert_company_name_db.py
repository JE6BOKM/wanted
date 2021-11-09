# myapp/management/commands/insert_company_name_db.py
from django.core.management.base import BaseCommand
from apps.company_info.models import CompanyName

class Command(BaseCommand):     
    help = 'insert data to company_names table'     

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('c_id_id', type=int)
        parser.add_argument('language_id', type=int)

    def handle(self, *args, **options):
        name = options['name']
        c_id_id = options['c_id_id']
        language_id = options['language_id']
        company_name = CompanyName(name=name, c_id_id=c_id_id, language_id=language_id)
        company_name.save()

        self.stdout.write('Successfully make company name "%s"' % name)