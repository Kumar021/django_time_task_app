# Generated by Django 3.1.2 on 2020-11-04 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20201104_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelookupevent',
            name='name',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
