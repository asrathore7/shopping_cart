# Generated by Django 3.2.9 on 2021-12-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_orderlines_saleorder_orderline_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleorder',
            name='amount_total',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
