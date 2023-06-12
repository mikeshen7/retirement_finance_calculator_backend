from django.urls import path
from .views import income_form, income_output

urlpatterns = [
    path('income_form', income_form.as_view(), name='income_form'),
    path('income_output', income_output.as_view(), name='income_output'),
]
