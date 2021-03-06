from django.contrib.auth.models import User
from django.db import models

bnull = dict(blank=True, null=True)

class Exame(models.Model):
    cod_exame = models.IntegerField('Codigo do exame ')
    descricao = models.CharField('Descrição do exame', max_length=120)

    def __str__(self):
        return self.descricao

    def __repr__(self):
        return self.id

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

class Consulta(models.Model):
    numero_guia_consulta = models.IntegerField('Número da Guia')
    cod_medico = models.IntegerField('Código médico')
    nome_medico = models.CharField('Nome do médico', max_length=120)
    data_consulta = models.DateField('Data da consulta')
    valor_consulta = models.DecimalField('Valor da consulta', max_digits=11, decimal_places=2, **bnull)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def num_exames(self):
        return self.exames.all().count()

    def valor_exames(self):
        soma = 0
        for exame in self.exames.all():
            soma += exame.valor_exame
        return soma

    def total_da_consulta(self):
        return self.valor_consulta+self.valor_exames()


class ExameRealizado(models.Model):
    exame = models.ForeignKey(Exame, related_name='realizados', on_delete=models.CASCADE)
    consulta = models.ForeignKey(Consulta, related_name='exames', on_delete=models.CASCADE)
    valor_exame = models.DecimalField('Valor do exame', max_digits=11, decimal_places=2, **bnull)

    class Meta:
        verbose_name = 'Exame realizado'
        verbose_name_plural = 'Exames realizados'

class Logdb(models.Model):
    post_req = models.TextField(verbose_name='Post to API, via request (Python)')
    post_curl = models.TextField(verbose_name='Post to API, via curl (CLI)')

    class Meta:
        verbose_name = 'Log Post'
        verbose_name_plural = 'Logs Posts'


    




