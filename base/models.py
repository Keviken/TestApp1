from django.db import models

class ExcelData(models.Model):
    file = models.FileField(upload_to='excel_files/')
    column1 = models.CharField(max_length=255)
    column2 = models.CharField(max_length=255)
    # Add more fields as per your requirements
