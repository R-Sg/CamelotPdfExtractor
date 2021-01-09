from django.urls import path
from extractpdfapp.views import extract_pdf, table_to_csv

urlpatterns = [
    path('extract_pdf_table/', extract_pdf),
    path('table_to_csv/', table_to_csv),
]
