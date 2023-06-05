from django.db import models


class Tax_Bracket(models.Model):

    # Option Selections
    tax_type_choices = [
        ('ordinary', 'Ordinary Income'),
        ('capital_gains', 'Capital Gaines'),
    ]
    filing_status_choices = [
        ('single', 'Single'),
        ('mfj', 'Married Filing Jointly'),
        ('mfs', 'Married Filing Separately'),
        ('hh', 'Head of Household'),
        ('qw', 'Qualifying Widow'),
    ]

    # Fields
    tax_type = models.CharField(
        max_length=32,
        choices=tax_type_choices,
        default='ordinary',
    )
    filing_status = models.CharField(
        max_length=32,
        choices=filing_status_choices,
        default='mfj',
    )
    bracket_order = models.IntegerField()
    lower_bound = models.DecimalField(max_digits=20, decimal_places=3)
    upper_bound = models.DecimalField(max_digits=20, decimal_places=3)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.year} {self.filing_status} {self.tax_type} {self.percentage}%'
