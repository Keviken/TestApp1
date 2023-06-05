from django import forms
from base.models import ExcelData

class ExcelDataForm(forms.ModelForm):
    class Meta:
        model = ExcelData
        fields = ('file',)
