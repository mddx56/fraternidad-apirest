# Generated by Django 4.2.3 on 2023-09-08 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='copy_ci',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='financial_condition',
            field=models.CharField(choices=[('normal', 'Normal'), ('plan', 'Plan de Pagos')], default='normal', max_length=17),
        ),
    ]
