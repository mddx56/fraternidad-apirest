# Generated by Django 4.2.7 on 2024-06-17 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agendas', '0007_detallepagoextraordianria_saldo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mes', models.SmallIntegerField(null=True)),
                ('pagado', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Extraord',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('concepto', models.TextField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='mensualidad',
            name='gestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agendas.gestion'),
        ),
        migrations.CreateModel(
            name='FraterExtraord',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('cuota_mensual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('extraord', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agendas.extraord')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetallePagoExtraord',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('cuota', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agendas.cuota')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendas.pago')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cuota',
            name='frater_extraord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agendas.fraterextraord'),
        ),
        migrations.AddField(
            model_name='cuota',
            name='gestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agendas.gestion'),
        ),
    ]
