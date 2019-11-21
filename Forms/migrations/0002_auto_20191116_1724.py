# Generated by Django 2.2.7 on 2019-11-16 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asigpregunta',
            name='formulario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forms.Formulario'),
        ),
        migrations.AlterField(
            model_name='asigpregunta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forms.Pregunta'),
        ),
    ]