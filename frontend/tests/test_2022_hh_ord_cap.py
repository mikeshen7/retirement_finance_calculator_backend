from django.test import TestCase
from django.urls import reverse
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class TaxCalculationTest(TestCase):
    def test_hh_ord_cap_0(self):
        # Prepare test data
        data = {
            'filing-status': 'hh',
            'tax-year': '2022',
            'ordinary-income': '10000',
            'capital-gains': '10000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('0'))
        self.assertEqual(context['capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['total_tax'], Decimal('0'))

    def test_hh_ord_cap_1(self):
        # Prepare test data
        data = {
            'filing-status': 'hh',
            'tax-year': '2022',
            'ordinary-income': '30000',
            'capital-gains': '10000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('1060'))
        self.assertEqual(context['capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['total_tax'], Decimal('1060'))

    def test_hh_ord_cap_2(self):
        # Prepare test data
        data = {
            'filing-status': 'hh',
            'tax-year': '2022',
            'ordinary-income': '600000',
            'capital-gains': '100000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('176277.50'))
        self.assertEqual(context['capital_gains_tax'], Decimal('20000'))
        self.assertEqual(context['total_tax'], Decimal('196277.50'))
