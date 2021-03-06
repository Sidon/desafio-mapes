# Generated by Django 2.1.5 on 2019-01-17 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_guia_consulta', models.IntegerField(verbose_name='Número da Guia')),
                ('cod_medico', models.IntegerField(verbose_name='Código médico')),
                ('nome_medico', models.CharField(max_length=120, verbose_name='Nome do médico')),
                ('data_consulta', models.DateField(verbose_name='Data da conulta')),
                ('valor_consulta', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='Valor da consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_exame', models.IntegerField(verbose_name='Codigo ExameRealizado')),
                ('descricao', models.CharField(max_length=120, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Exame',
                'verbose_name_plural': 'Exames',
            },
        ),
        migrations.CreateModel(
            name='ExameRealizado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_exame', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='Valor d exame')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exames', to='core.Consulta')),
                ('exame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realizados', to='core.Exame')),
            ],
            options={
                'verbose_name': 'Exame realizado',
                'verbose_name_plural': 'Exames realizados',
            },
        ),
        migrations.CreateModel(
            name='Logdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_req', models.TextField(verbose_name='Post to API, via request (Python)')),
                ('post_curl', models.TextField(verbose_name='Post to API, via curl (CLI)')),
            ],
            options={
                'verbose_name': 'Log Post',
                'verbose_name_plural': 'Logs Posts',
            },
        ),
    ]
