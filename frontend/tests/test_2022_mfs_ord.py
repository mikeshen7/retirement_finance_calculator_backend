from django.test import TestCase
from django.urls import reverse
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class TaxCalculationTest(TestCase):
    def test_mfs_ord_0(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '10000',
            'capital-gains': '0',
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

    def test_mfs_ord_10(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '15000',
            'capital-gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('205'))
        self.assertEqual(context['capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['total_tax'], Decimal('205'))

    def test_mfs_ord_12(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '20000',
            'capital-gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('705'))
        self.assertEqual(context['capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['total_tax'], Decimal('705'))

    def test_mfs_ord_22(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '60000',
            'capital-gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('5968'))
        self.assertEqual(context['capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['total_tax'], Decimal('5968'))

    def test_mfs_ord_24(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '110000',
            'capital-gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('17127.48'))
        self.assertEqual(context['capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['total_tax'], Decimal('17127.48'))

    def test_mfs_ord_32(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '190000',
            'capital-gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('36887.48'))
        self.assertEqual(context['capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['total_tax'], Decimal('36887.48'))

    def test_mfs_ord_35(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '230000',
            'capital-gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('49720.48'))
        self.assertEqual(context['capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['total_tax'], Decimal('49720.48'))

    def test_mfs_ord_37(self):
        # Prepare test data
        data = {
            'filing-status': 'mfs',
            'tax-year': '2022',
            'ordinary-income': '350000',
            'capital-gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['ordinary_income_tax'], Decimal('91982.98'))
        self.assertEqual(context['capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['total_tax'], Decimal('91982.98'))

