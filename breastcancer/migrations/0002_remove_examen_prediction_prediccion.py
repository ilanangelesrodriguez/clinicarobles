# Generated by Django 5.0.9 on 2024-11-12 02:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breastcancer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examen',
            name='prediction',
        ),
        migrations.CreateModel(
            name='Prediccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction', models.CharField(choices=[('B', 'Benigno'), ('M', 'Maligno')], max_length=1)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predicciones', to='breastcancer.examen')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='breastcancer.modelo')),
            ],
            options={
                'verbose_name_plural': 'Exámenes',
            },
        ),
    ]
