# Generated by Django 4.2.7 on 2024-04-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0006_remove_detallepagoextraordianria_deuda_extraordinaria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallepagoextraordianria',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
