import os
import csv
from dateutil import parser
from django.core.management.base import BaseCommand
from  core.models import Consulta, ExameRealizado, Exame, Logdb
from django.contrib.auth.models import User
from django.db.models import Q
from util.logapi import Log_api
from sdnmapes import settings

def read_csv(file_name):
    fname = os.path.join(settings.DOC, file_name)
    lst = []
    if os.path.exists(fname):
        with open(fname, newline='') as f:
            try:
                reader = csv.reader(f, delimiter=';')
                for row in reader:
                    lst.append(row)
            except :
                print('Erro na abertura do arquivo')

    else:
        print('Arquivo não encontrado')
        return None
    return lst

consultas = read_csv('consulta.csv')
exames_realizados = read_csv('exame.csv')

exames = {}
for exame in exames_realizados:
    key = exame[0]
    descricao = 'ExameRealizado Laboratorial ' + exame[0]
    if not key in exames:
        exames[key] = descricao


class Command(BaseCommand):
    help = 'Create initial data'
    log_api = Log_api()

    def handle(self, *args, **options):
        if User.objects.filter(Q(username='admin') & Q(is_superuser=1)):
            Consulta.objects.all().delete()
            ExameRealizado.objects.all().delete()
            Logdb.objects.all().delete()
            
            for exame in exames:
                Exame.objects.create(cod_exame=exame, descricao=exames[exame])
 
            for consulta in consultas:
               data_consulta = str(parser.parse(consulta[3]))[0:10]
               Consulta.objects.create(
                    numero_guia_consulta=consulta[0], cod_medico=consulta[1],
                                        nome_medico=consulta[2], data_consulta=data_consulta, valor_consulta=consulta[4])

            for realizado in exames_realizados:
                consulta = Consulta.objects.get(numero_guia_consulta=realizado[1])
                exame = Exame.objects.filter(cod_exame=realizado[0]).order_by('id').first()
                ExameRealizado.objects.create(exame=exame, consulta=consulta, valor_exame=realizado[2])

        else:
            print('Inclua um usuário superuser com o nome admin')








