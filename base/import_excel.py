import openpyxl
from base.models import ExcelData

def import_data_from_excel(file):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        excel_data = ExcelData(column1=row[0], column2=row[1], file=file.name)
        excel_data.save()
