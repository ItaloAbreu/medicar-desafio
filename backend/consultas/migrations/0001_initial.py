# Generated by Django 3.2.7 on 2021-09-26 19:32

import consultas.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(validators=[consultas.models.date_in_the_past])),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicos.medico')),
            ],
            options={
                'unique_together': {('medico', 'dia')},
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_agendamento', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('dia', models.DateField()),
                ('horario', models.TimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicos.medico')),
            ],
            options={
                'ordering': ['dia', 'horario'],
            },
        ),
        migrations.CreateModel(
            name='HorarioAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.agenda')),
            ],
            options={
                'unique_together': {('horario', 'agenda')},
            },
        ),
    ]
