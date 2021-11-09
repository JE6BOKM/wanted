import os
import django
import csv
import sys
import configurations

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
configurations.setup()


from apps.company_info.models import Company, CompanyName, Language, Tag

CSV_PATH_COMPANYS = './csv/company_name.csv'

with open(CSV_PATH_COMPANYS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        company_name = row[0]       
        c_id = row[1]
        lang_id = row[2]

        CompanyName.objects.create(name=company_name, c_id_id=c_id, language_id=lang_id)
