from django.shortcuts import render
from base.forms import ExcelDataForm
from base.import_excel import import_data_from_excel


def import_excel_view(request):
    if request.method == 'POST':
        form = ExcelDataForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            import_data_from_excel(file)
    else:
        form = ExcelDataForm()

    return render(request, 'import_excel.html', {'form': form})
