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
        tax_filing_status = request.POST.get('tax_filing_status')
        tax_tax_year = request.POST.get('tax_tax_year')

        # Get ordinary income and handle invalid input
        try:
            tax_ordinary_income = int(request.POST.get('tax_ordinary_income'))
        except ValueError:
            tax_ordinary_income = 0

        try:
            tax_capital_gains = int(request.POST.get('tax_capital_gains'))
        except ValueError:
            tax_capital_gains = 0

        # Get data from database
        tax_ordinary_income_bracket, tax_capital_gains_bracket, tax_standard_deduction = get_tax_brackets(
            tax_tax_year, tax_filing_status)

        # Calc taxable income
        tax_taxable_ordinary_income, tax_taxable_capital_gains = calculate_taxable_income(
            tax_ordinary_income, tax_capital_gains, tax_standard_deduction)

        # Calculate tax on ordinary income
        tax_ordinary_income_tax = calculate_tax(
            tax_taxable_ordinary_income, tax_ordinary_income_bracket)

        # Find capital gains starting tax bracket
        tax_tax_bracket_index = find_capital_gains_bracket(
            tax_taxable_ordinary_income, tax_capital_gains_bracket)
        tax_capital_gains_tax = calculate_tax(
            tax_taxable_capital_gains, tax_capital_gains_bracket, tax_tax_bracket_index, tax_taxable_ordinary_income)

        tax_total_tax = tax_ordinary_income_tax + tax_capital_gains_tax

        # Prepare the context data to be passed to the template
        context = {
            'tax_filing_status': tax_filing_status,
            'tax_tax_year': tax_tax_year,
            'tax_ordinary_income': tax_ordinary_income,
            'tax_capital_gains': tax_capital_gains,
            'tax_standard_deduction': tax_standard_deduction,
            'tax_ordinary_income_bracket': tax_ordinary_income_bracket,
            'tax_capital_gains_bracket': tax_capital_gains_bracket,
            'tax_taxable_ordinary_income': tax_taxable_ordinary_income,
            'tax_taxable_capital_gains': tax_taxable_capital_gains,
            'tax_ordinary_income_tax': tax_ordinary_income_tax,
            'tax_capital_gains_tax': tax_capital_gains_tax,
            'tax_total_tax': tax_total_tax,
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
