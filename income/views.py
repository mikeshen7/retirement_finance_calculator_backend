from django.views.generic import TemplateView
from django.shortcuts import render
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal

class income_form(TemplateView):
    template_name = 'income_form.html'

class income_output(TemplateView):
    template_name = 'income_output.html'

    def post(self, request, *args, **kwargs):

        # Get data from form
        try:
            income_wages = int(request.POST.get('income_wages'))
        except ValueError:
            income_wages = 0

        try:
            income_wages_period = request.POST.get('income_wages_period')
        except ValueError:
            income_wages_period = 'annually'

        try:
            income_dividend = int(request.POST.get('income_dividend'))
        except ValueError:
            income_dividend = 0

        try:
            income_interest = int(request.POST.get('income_interest'))
        except ValueError:
            income_interest = 0

        try:
            income_pension = int(request.POST.get('income_pension'))
        except ValueError:
            income_pension = 0

        try:
            income_social_security = int(request.POST.get('income_social_security'))
        except ValueError:
            income_social_security = 0

        try:
            income_other_income = int(request.POST.get('income_other_income'))
        except ValueError:
            income_other_income = 0

        # Convert to annual income

        # Total
        income_total_income = 0

        # Prepare the context data to be passed to the template
        context = {
            'income_wages': income_wages,
            'income_wages_period': income_wages_period,
            'income_dividend': income_dividend,
            'income_interest': income_interest,
            'income_pension': income_pension,
            'income_social_security': income_social_security,
            'income_other_income': income_other_income,
            'income_total_income': income_total_income,
        }

        return render(request, self.template_name, context)
