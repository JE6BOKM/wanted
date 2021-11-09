# myapp/management/commands/insert_company_db.py
from django.core.management.base import BaseCommand
from apps.company_info.models import Company

class Command(BaseCommand):     
    help = 'insert data to companies table'     

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)

    def handle(self, *args, **options):
        id = options['id']
        company = Company(id=id)
        company.save()

        self.stdout.write('Successfully make company "%s"' % id)