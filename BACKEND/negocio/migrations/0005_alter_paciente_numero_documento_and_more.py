# Generated by Django 5.2.4 on 2025-07-29 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0004_alter_paciente_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='numero_documento',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tipo_documento',
            field=models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('TI', 'Tarjeta de identidad'), ('CE', 'Cédula de extranjería')], default='CC', max_length=2, null=True),
        ),
    ]
