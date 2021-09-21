# Generated by Django 3.2.7 on 2021-09-21 01:54

from django.db import migrations, models
import django.db.models.deletion
import medicos.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=240)),
                ('crm', models.CharField(max_length=13, validators=[medicos.models.validar_crm])),
                ('email', models.EmailField(max_length=254)),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('especialidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicos.especialidade')),
            ],
        ),
    ]
