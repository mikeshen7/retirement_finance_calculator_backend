# Generated by Django 4.2.1 on 2023-06-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_class', models.CharField(default='None', max_length=128)),
                ('year', models.IntegerField()),
                ('annual_return', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
