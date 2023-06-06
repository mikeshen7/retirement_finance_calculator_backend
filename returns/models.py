from django.db import models


class Return(models.Model):
    # Fields
    asset_class = models.CharField(max_length=128, default='None',)
    year = models.IntegerField()
    annual_return = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.year} {self.asset_class} {self.tax_type} {self.annual_return}%'
