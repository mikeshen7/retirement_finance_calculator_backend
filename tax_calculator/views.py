from django.views.generic import TemplateView
from django.shortcuts import render
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class tax_calc_form(TemplateView):
    template_name = 'tax_calc_form.html'


class tax_calc_output(TemplateView):
    template_name = 'tax_calc_output.html'

    def post(self, request, *args, **kwargs):

        # Get data from form
        filing_status = request.POST.get('filing-status')
        tax_year = request.POST.get('tax-year')

        # Get ordinary income and handle invalid input
        try:
            ordinary_income = int(request.POST.get('ordinary-income'))
        except ValueError:
            ordinary_income = 0

        try:
            capital_gains = int(request.POST.get('capital-gains'))
        except ValueError:
            capital_gains = 0

        # Get data from database
        ordinary_income_bracket, capital_gains_bracket, standard_deduction = get_tax_brackets(
            tax_year, filing_status)

        # Calc taxable income
        taxable_ordinary_income, taxable_capital_gains = calculate_taxable_income(
            ordinary_income, capital_gains, standard_deduction)

        # Calculate tax on ordinary income
        ordinary_income_tax = calculate_tax(
            taxable_ordinary_income, ordinary_income_bracket)

        # Find capital gains starting tax bracket
        tax_bracket_index = find_capital_gains_bracket(
            taxable_ordinary_income, capital_gains_bracket)
        capital_gains_tax = calculate_tax(
            taxable_capital_gains, capital_gains_bracket, tax_bracket_index, taxable_ordinary_income)

        total_tax = ordinary_income_tax + capital_gains_tax

        # Prepare the context data to be passed to the template
        context = {
            'filing_status': filing_status,
            'tax_year': tax_year,
            'ordinary_income': ordinary_income,
            'capital_gains': capital_gains,
            'standard_deduction': standard_deduction,
            'ordinary_income_bracket': ordinary_income_bracket,
            'capital_gains_bracket': capital_gains_bracket,
            'taxable_ordinary_income': taxable_ordinary_income,
            'taxable_capital_gains': taxable_capital_gains,
            'ordinary_income_tax': ordinary_income_tax,
            'capital_gains_tax': capital_gains_tax,
            'total_tax': total_tax,
        }

        return render(request, self.template_name, context)


def get_tax_brackets(tax_year, filing_status):
    ordinary_income_bracket = Tax_Bracket.objects.filter(year=tax_year, filing_status=filing_status,
                                                         tax_type='ordinary')
    capital_gains_bracket = Tax_Bracket.objects.filter(year=tax_year, filing_status=filing_status,
                                                       tax_type='capital_gains')
    standard_deduction = Deduction.objects.filter(year=tax_year, filing_status=filing_status)[0].deduction
    return ordinary_income_bracket, capital_gains_bracket, standard_deduction


def calculate_taxable_income(ordinary_income, capital_gains, standard_deduction):
    if ordinary_income <= standard_deduction:
        taxable_ordinary_income = 0
        taxable_capital_gains = capital_gains - (standard_deduction - ordinary_income)
        if taxable_capital_gains < 0:
            taxable_capital_gains = 0
    else:
        taxable_ordinary_income = ordinary_income - standard_deduction
        taxable_capital_gains = capital_gains

    return taxable_ordinary_income, taxable_capital_gains


def calculate_tax(income, tax_brackets, tax_bracket_index=0, old_taxable_ordinary_income=0):
    # Calculate tax on ordinary income
    tax = Decimal(0)

    while income > 0:
        # Protects against infinite loop
        if tax_bracket_index > 100:
            break

        lower_bound = max(
            tax_brackets[tax_bracket_index].lower_bound, old_taxable_ordinary_income)
        upper_bound = tax_brackets[tax_bracket_index].upper_bound
        percentage = tax_brackets[tax_bracket_index].percentage
        bracket_size = upper_bound - lower_bound

        if income <= bracket_size:
            tax += income * percentage / 100
            income = 0
        else:
            tax += bracket_size * percentage / 100
            income -= bracket_size
            tax_bracket_index += 1
    return tax.quantize(Decimal('0'))


def find_capital_gains_bracket(taxable_ordinary_income, capital_gains_bracket):
    tax_bracket_index = 0
    upper_bound = capital_gains_bracket[tax_bracket_index].upper_bound

    while taxable_ordinary_income > upper_bound:
        # Protects against infinite loop
        if tax_bracket_index > 100:
            break

        tax_bracket_index += 1
        upper_bound = capital_gains_bracket[tax_bracket_index].upper_bound

    return tax_bracket_index
