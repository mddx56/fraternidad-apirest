# Generated by Django 4.2.7 on 2024-10-03 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='cronograma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='config.cronograma'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='dia_semana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='config.diasemana'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='config.horario'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='fraternidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='config.fraternidad'),
        ),
        migrations.AlterField(
            model_name='mediaimage',
            name='fraternidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='config.fraternidad'),
        ),
        migrations.AlterField(
            model_name='mediavideo',
            name='fraternidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='config.fraternidad'),
        ),
    ]
