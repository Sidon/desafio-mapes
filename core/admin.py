from django.contrib import admin
from core.models import Consulta, ExameRealizado

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
    list_display = ['numero_guia_consulta', 'cod_medico', 'data_consulta', 'valor_consulta']
    list_display_links = list_display
    search_fields = ['numero_guia_consulta']
    list_filter = ['cod_medico', 'data_consulta']
    inlines = (ExamesInline,)
    list_per_page = LIST_PER_PAGE

@admin.register(ExameRealizado)
class ExameRealizadoAdmin(admin.ModelAdmin):
    list_display = ['exame', 'consulta', 'valor_exame']
    list_display_links = list_display
    search_fields = ['consulta']
    list_per_page = LIST_PER_PAGE
