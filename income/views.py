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
            income = int(request.POST.get('income'))
        except ValueError:
            income = 0

        try:
            dividend = int(request.POST.get('dividend'))
        except ValueError:
            dividend = 0

        try:
            interest = int(request.POST.get('interest'))
        except ValueError:
            interest = 0

        try:
            pension = int(request.POST.get('pension'))
        except ValueError:
            pension = 0

        try:
            social_security = int(request.POST.get('social_security'))
        except ValueError:
            social_security = 0

        try:
            other_income = int(request.POST.get('other_income'))
        except ValueError:
            other_income = 0

        # Convert to annual income

        # Total
        total_income = 0

        # Prepare the context data to be passed to the template
        context = {
            'income': income,
            'dividend': dividend,
            'interest': interest,
            'pension': pension,
            'social_security': social_security,
            'other_income': other_income,
            'total_income': total_income,
        }

        return render(request, self.template_name, context)
