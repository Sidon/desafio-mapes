from django.contrib import admin
from core.models import Consulta, Exame, ExameRealizado

__author__ = "Sidon Duarte"
__date__ = "Created by 18/01/19"
__copyright__ = "Copyright 2019"
__email__ = "sidoncd@gmail.com"

LIST_PER_PAGE = 10

class ExamesInline(admin.TabularInline):
    model = ExameRealizado
    extra = 1

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['numero_guia_consulta', 'cod_medico', 'data_consulta', 'num_exames','valor_exames',
                    'valor_consulta', 'total_da_consulta']
    list_display_links = list_display
    search_fields = ['numero_guia_consulta']
    list_filter = ['cod_medico', 'data_consulta']
    inlines = (ExamesInline,)
    list_per_page = LIST_PER_PAGE

@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    list_display = ['cod_exame', 'descricao']
    list_display_links = list_display
    search_fields = ['descricao']
    list_per_page = LIST_PER_PAGE

@admin.register(ExameRealizado)
class ExameRealizadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'guia_consulta','exame_realizado', 'valor_exame')
    list_per_page = LIST_PER_PAGE

    def guia_consulta(self, instance):
        return instance.consulta.numero_guia_consulta

    def exame_realizado(self, instance):
        return instance.exame.descricao