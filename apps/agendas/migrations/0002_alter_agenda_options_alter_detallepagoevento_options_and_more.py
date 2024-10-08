# Generated by Django 4.2.7 on 2024-09-27 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelOptions(
            name='detallepagoevento',
            options={'verbose_name': 'Detalle Pago Evento', 'verbose_name_plural': 'Detalles Pago Evento'},
        ),
        migrations.AlterModelOptions(
            name='detallepagoextraordianria',
            options={'verbose_name': 'Detalle Pago Extraordianria', 'verbose_name_plural': 'Detalles Pago Extraordianria'},
        ),
        migrations.AlterModelOptions(
            name='detallepagomensualidad',
            options={'verbose_name': 'Detalle Pago Mensualidad', 'verbose_name_plural': 'Detalles Pago Mensualidad'},
        ),
        migrations.AlterModelOptions(
            name='extraordinaria',
            options={'verbose_name': 'Extraordinaria', 'verbose_name_plural': 'Extraordinarias'},
        ),
        migrations.AlterModelOptions(
            name='gestion',
            options={'verbose_name': 'Gestion', 'verbose_name_plural': 'Gestiones'},
        ),
        migrations.AlterModelOptions(
            name='mensualidad',
            options={'verbose_name': 'Mensualidad', 'verbose_name_plural': 'Mensualidades'},
        ),
        migrations.AlterModelOptions(
            name='tipoevento',
            options={'verbose_name': 'Tipo de Evento', 'verbose_name_plural': 'Tipos de Evento'},
        ),
        migrations.AlterField(
            model_name='agenda',
            name='descripcion',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='es_entresemana',
            field=models.BooleanField(default=False, verbose_name='Entre semana'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='estado_reserva',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('activa', 'Activa'), ('rechazada', 'Rechazada')], default='pendiente', max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='tipo_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agendas.tipoevento', verbose_name='Tipo de evento'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Fraterno'),
        ),
        migrations.AlterField(
            model_name='detallepagoevento',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendas.agenda', verbose_name='Evento'),
        ),
        migrations.AlterField(
            model_name='detallepagoevento',
            name='pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendas.pago', verbose_name='Pago'),
        ),
        migrations.AlterField(
            model_name='extraordinaria',
            name='concepto',
            field=models.TextField(default='', verbose_name='Concepto'),
        ),
        migrations.AlterField(
            model_name='extraordinaria',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto'),
        ),
        migrations.AlterField(
            model_name='gestion',
            name='anio',
            field=models.IntegerField(default=-1, verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='gestion',
            name='en_curso',
            field=models.BooleanField(verbose_name='En curso?'),
        ),
        migrations.AlterField(
            model_name='qr',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='qr',
            name='qr_valor',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto de QR'),
        ),
        migrations.AlterField(
            model_name='qr',
            name='tipo_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendas.tipoevento', verbose_name='Tipo de Evento'),
        ),
        migrations.AlterField(
            model_name='qr',
            name='url',
            field=models.URLField(default='', max_length=700, verbose_name='Url de QR'),
        ),
        migrations.AlterField(
            model_name='tipoevento',
            name='costo_entresemana',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Costo entre semana'),
        ),
        migrations.AlterField(
            model_name='tipoevento',
            name='costo_finsemana',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Costo fin semana'),
        ),
        migrations.AlterField(
            model_name='tipoevento',
            name='descripcion',
            field=models.TextField(default='', null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='tipoevento',
            name='nombre',
            field=models.CharField(default='', max_length=100, verbose_name='Nombre'),
        ),
    ]
