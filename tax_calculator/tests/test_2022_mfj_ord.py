from django.test import TestCase
from django.urls import reverse
from tax_brackets.models import Tax_Bracket
from deductions.models import Deduction
from decimal import Decimal


class TaxCalculationTest(TestCase):
    def test_mfj_ord_0(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
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
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('0'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('0'))

    def test_mfj_ord_10(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
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
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('410'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('410'))

    def test_mfj_ord_12(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '80000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('6081'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('6081'))

    def test_mfj_ord_22(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '120000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('11936'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('11936'))

    def test_mfj_ord_24(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '210000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('31855'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('31855'))

    def test_mfj_ord_32(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '370000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('70575'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('70575'))

    def test_mfj_ord_35(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '460000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('99441'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('99441'))

    def test_mfj_ord_37(self):
        # Prepare test data
        data = {
            'tax_filing_status': 'mfj',
            'tax_tax_year': '2022',
            'tax_ordinary_income': '680000',
            'tax_capital_gains': '0',
        }

        # Send POST request to the view
        response = self.client.post(reverse('tax_calc_output'), data=data)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check tax calculations in the response context
        context = response.context
        self.assertEqual(context['tax_ordinary_income_tax'], Decimal('176566'))
        self.assertEqual(context['tax_capital_gains_tax'], Decimal('0'))
        self.assertEqual(context['tax_total_tax'], Decimal('176566'))

