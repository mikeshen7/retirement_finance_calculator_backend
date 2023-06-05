from django.db import models


class Deduction(models.Model):
    # Option Selections
    filing_status_choices = [
        ('single', 'Single'),
        ('mfj', 'Married Filing Jointly'),
        ('mfs', 'Married Filing Separately'),
        ('hh', 'Head of Household'),
        ('qw', 'Qualifying Widow'),
    ]

    # Fields
    year = models.IntegerField()
    filing_status = models.CharField(
        max_length=32,
        choices=filing_status_choices,
        default='mfj',
    )
    deduction = models.IntegerField()


    def __str__(self):
        return f'{self.year} {self.filing_status} {self.deduction}'
