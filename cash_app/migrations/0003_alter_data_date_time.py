# Generated by Django 4.2.1 on 2023-05-23 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_app', '0002_data_remove_debitdata_user_delete_creditdata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date_time',
            field=models.DateTimeField(verbose_name='Date'),
        ),
    ]