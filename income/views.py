from django.views.generic import TemplateView
from django.shortcuts import render
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class income_form(TemplateView):
    template_name = 'income_form.html'


class income_output(TemplateView):
    template_name = 'income_output.html'
