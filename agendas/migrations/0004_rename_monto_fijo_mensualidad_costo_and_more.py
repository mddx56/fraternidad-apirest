# Generated by Django 4.2.3 on 2023-09-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0003_alter_deuda_estado_deuda_delete_estadodeuda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensualidad',
            old_name='monto_fijo',
            new_name='costo',
        ),
        migrations.RenameField(
            model_name='tipoevento',
            old_name='precio',
            new_name='costo_entresemana',
        ),
        migrations.RemoveField(
            model_name='qr',
            name='deuda',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='fecha',
        ),
        migrations.AddField(
            model_name='mensualidad',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='qr',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='qr',
            name='url',
            field=models.URLField(default='', max_length=700),
        ),
        migrations.AddField(
            model_name='tipoevento',
            name='costo_finsemana',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='turno',
            name='fecha_antigua',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='turno',
            name='fecha_nueva',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turno',
            name='nro_semana',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]