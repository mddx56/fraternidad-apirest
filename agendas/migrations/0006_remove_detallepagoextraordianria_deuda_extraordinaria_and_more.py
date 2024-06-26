# Generated by Django 4.2.7 on 2024-04-07 21:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("agendas", "0005_delete_turnopl"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="detallepagoextraordianria",
            name="deuda_extraordinaria",
        ),
        migrations.AddField(
            model_name="detallepagoextraordianria",
            name="extraordinaria",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="agendas.extraordinaria",
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="DeudaExtraordinaria",
        ),
    ]
