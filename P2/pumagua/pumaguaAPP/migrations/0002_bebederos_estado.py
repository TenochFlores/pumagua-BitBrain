# Generated by Django 4.1.6 on 2024-04-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumaguaAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bebederos',
            name='estado',
            field=models.CharField(choices=[('0', 'No disponible'), ('1', 'Disponible'), ('2', 'En mantenimiento')], default='1', max_length=1),
        ),
    ]
