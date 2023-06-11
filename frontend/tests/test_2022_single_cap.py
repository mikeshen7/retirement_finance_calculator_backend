from django.test import TestCase
from django.urls import reverse
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class TaxCalculationTest(TestCase):
    def test_single_cap_0(self):
        # Prepare test data
        data = {
            'filing-status': 'single',
            'tax-year': '2022',
            'ordinary-income': '0',
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

    def test_single_cap_1(self):
        # Prepare test data
        data = {
            'filing-status': 'single',
            'tax-year': '2022',
            'ordinary-income': '0',
            'capital-gains': '64625',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('0'))
        self.assertEqual(context['capital_gains_tax'], Decimal('1500'))
        self.assertEqual(context['total_tax'], Decimal('1500'))

    def test_single_cap_2(self):
        # Prepare test data
        data = {
            'filing-status': 'single',
            'tax-year': '2022',
            'ordinary-income': '0',
            'capital-gains': '482700',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('0'))
        self.assertEqual(context['capital_gains_tax'], Decimal('64711.25'))
        self.assertEqual(context['total_tax'], Decimal('64711.25'))
