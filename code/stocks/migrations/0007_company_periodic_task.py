# Generated by Django 3.1.2 on 2020-11-07 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0014_remove_clockedschedule_enabled'),
        ('stocks', '0006_company_has_granular_scraping'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='periodic_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_beat.periodictask'),
        ),
    ]
