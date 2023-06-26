from django.test import TestCase
from django.urls import reverse
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class TaxCalculationTest(TestCase):
    def test_hh_ord_0(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '15000',
            'tax_capital_gains': '0',
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

    def test_hh_ord_10(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '30000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('1060'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('1060'))

    def test_hh_ord_12(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '35000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('1579'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('1579'))

    def test_hh_ord_22(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '75000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('6379'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('6379'))

    def test_hh_ord_24(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '110000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('14080'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('14080'))

    def test_hh_ord_32(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '190000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('33324'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('33324'))

    def test_hh_ord_35(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '235000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('47724'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('47724'))

    def test_hh_ord_37(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'hh',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '560000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('161478'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('161478'))

