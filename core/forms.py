from django.forms import ModelForm
import django_filters
from .models import Consulta, ExameRealizado

class ConsultaFilter(django_filters.FilterSet):
    class Meta:
        model = Consulta
        fields = ('numero_guia_consulta','cod_medico',)

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta

        fields = ['numero_guia_consulta', 'cod_medico', 'nome_medico', 'data_consulta',
                  'valor_consulta']

class ExameForm(ModelForm):
    class Meta:
        model = ExameRealizado
        fields = ['consulta', 'valor_exame']
