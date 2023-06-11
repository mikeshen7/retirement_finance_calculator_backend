from django.test import TestCase
from django.urls import reverse
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class TaxCalculationTest(TestCase):
    def test_mfs_ord_cap_0(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
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

    def test_mfs_ord_cap_1(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '100000',
            'capital-gains': '100000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('14768'))
        self.assertEqual(context['capital_gains_tax'], Decimal('15000'))
        self.assertEqual(context['total_tax'], Decimal('29768'))

    def test_mfs_ord_cap_2(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '400000',
            'capital-gains': '100000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('110482.98'))
        self.assertEqual(context['capital_gains_tax'], Decimal('20000'))
        self.assertEqual(context['total_tax'], Decimal('130482.98'))
