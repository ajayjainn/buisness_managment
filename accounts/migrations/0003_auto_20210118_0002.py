# Generated by Django 3.1.4 on 2021-01-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210117_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phoneNo',
            field=models.CharField(blank=True, default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='remarks',
            field=models.CharField(blank=True, default='', max_length=250),
            preserve_default=False,
        ),
    ]
