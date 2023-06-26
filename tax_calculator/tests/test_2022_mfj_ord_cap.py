from django.test import TestCase
from django.urls import reverse
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class TaxCalculationTest(TestCase):
    def test_mfj_ord_cap_0(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '20000',
            'tax_capital_gains': '5000',
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

    def test_mfj_ord_cap_1(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '50000',
            'tax_capital_gains': '10000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('2481'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('2481'))

    def test_mfj_ord_cap_2(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '700000',
            'tax_capital_gains': '100000',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('183966'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('20000'))
        self.assertEqual(context['tax_total_tax'], Decimal('203966'))
