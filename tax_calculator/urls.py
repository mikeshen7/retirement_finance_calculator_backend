from django.urls import path
from .views import tax_calc_form, tax_calc_output

urlpatterns = [
    path('tax_calc_form', tax_calc_form.as_view(), name='tax_calc_form'),
    path('tax_calc_output', tax_calc_output.as_view(), name='tax_calc_output'),
]
