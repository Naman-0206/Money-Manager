# Generated by Django 4.2.1 on 2023-05-23 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cash_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField(verbose_name='Date')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('info', models.CharField(max_length=100, verbose_name='Info')),
                ('type', models.CharField(max_length=10, verbose_name='Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='debitdata',
            name='user',
        ),
        migrations.DeleteModel(
            name='CreditData',
        ),
        migrations.DeleteModel(
            name='DebitData',
        ),
    ]