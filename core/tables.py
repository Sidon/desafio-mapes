from django.urls import reverse
import django_tables2 as tables
from django_tables2.utils import A
from .models import Consulta, ExameRealizado, Logdb

class ConsultaTable(tables.Table):
    numero_guia_consulta = tables.LinkColumn(args=[A('pk')], attrs={'class': 'edit'}, viewname='core:update1')

    class Meta:
        # template_name = "django_tables2/bootstrap4.html"
        template_name = "core/dt2_bs4.html"

        model = Consulta
        fields = ('numero_guia_consulta','cod_medico', 'nome_medico', 'data_consulta', 'valor_consulta')
        attrs = {"class": "table table-hover", 'thead': {'class': "thead-inverse"}  }
        empty_text = "Não encontrado!"
        exclude = ("friendly",)


class ExamesTable(tables.Table):
    id = tables.LinkColumn(args=[A('pk')], attrs={'class': 'edit'}, viewname='core:update-exame')
    guia = tables.Column(accessor='consulta.numero_guia_consulta')
    exame = tables.Column(accessor='exame.descricao')

    class Meta:
        # template_name = "django_tables2/bootstrap4.html"
        template_name = "core/dt2_bs4.html"
        model = ExameRealizado
        attrs = {"class": "table table-hover", 'thead': {'class': "thead-inverse"}  }
        empty_text = "Não encontrado!"
        sequence =  ('id', 'exame', 'guia' ,'valor_exame')
        exclude = ('consulta',)


class LogdbTable(tables.Table):
    class Meta:
        template_name = "core/dt2_bs4.html"
        model = Logdb
        fields = ('id','post_req','post_curl')
        attrs = {"class": "table table-hover", 'thead': {'class': "thead-inverse"}}
        empty_text = "Não encontrado!"


class Bootstrap4Table(tables.Table):
    country = tables.Column(linkify=True)
    continent = tables.Column(accessor="country.continent", linkify=True)

    class Meta:
        model = Consulta
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-hover" }
        exclude = ("friendly",)
