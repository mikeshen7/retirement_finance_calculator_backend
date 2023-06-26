from django.test import TestCase
from django.urls import reverse
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class TaxCalculationTest(TestCase):
    def test_hh_cap_0(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '0',
            'tax_capital_gains': '40000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('0'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('0'))

    def test_hh_cap_15(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '0',
            'tax_capital_gains': '80000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('0'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('720'))
        self.assertEqual(context['tax_total_tax'], Decimal('720'))

    def test_hh_cap_20(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '0',
            'tax_capital_gains': '600000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('0'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('83325'))
        self.assertEqual(context['tax_total_tax'], Decimal('83325'))

