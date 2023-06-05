from django.core.management.base import BaseCommand
from base.import_excel import import_data_from_excel
from base.forms import ExcelDataForm

class Command(BaseCommand):
    help = 'Import data from Excel'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        form = ExcelDataForm({'file': open(file_path, 'rb')})
        if form.is_valid():
            file = form.cleaned_data['file']
            import_data_from_excel(file)
