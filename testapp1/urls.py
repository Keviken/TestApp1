#from django.contrib import admin
from django.urls import path
from base.views import import_excel_view


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('import-excel/', import_excel_view, name='import-excel'),
    path('', import_excel_view, name='import-excel'),  # Add this line
    # Other URL patterns in your project
]
