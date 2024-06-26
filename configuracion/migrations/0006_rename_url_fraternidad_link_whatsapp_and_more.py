# Generated by Django 4.2.7 on 2024-04-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0005_mediavideo_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fraternidad',
            old_name='url',
            new_name='link_whatsapp',
        ),
        migrations.AddField(
            model_name='fraternidad',
            name='descripcion',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='fraternidad',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mediaimage',
            name='tag',
            field=models.CharField(default='', null=True),
        ),
    ]
