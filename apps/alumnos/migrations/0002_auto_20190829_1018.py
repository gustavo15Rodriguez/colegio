# Generated by Django 2.2.4 on 2019-08-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='codigo_postal',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(max_length=12),
        ),
    ]