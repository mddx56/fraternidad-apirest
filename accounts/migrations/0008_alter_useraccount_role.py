# Generated by Django 4.2.7 on 2024-04-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_useraccount_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='role',
            field=models.CharField(choices=[('Fraterno', 'fraterno'), ('Admin', 'admin'), ('Tesorero', 'tesorero'), ('Encargado', 'encargado')], default='Fraterno', max_length=15),
        ),
    ]