from django.test import TestCase
from django.urls import reverse
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class TaxCalculationTest(TestCase):
    def test_single_ord_0(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'single',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '10000',
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

    def test_single_ord_10(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'single',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '20000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('705'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('705'))

    def test_single_ord_12(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'single',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '33225',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('2228'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('2228'))

    def test_single_ord_22(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'single',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '64725',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('7008'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('7008'))

    def test_single_ord_24(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'single',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '112025',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('17614'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('17614'))

    def test_single_ord_32(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'single',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '193000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('37848'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('37848'))

    def test_single_ord_35(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'single',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '238900',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('52836'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('52836'))

    def test_single_ord_37(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'single',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '562850',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('166418'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('166418'))
