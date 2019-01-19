from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Consulta, Logdb, ExameRealizado
from rest_framework_tracking.models import APIRequestLog


class ConsultaSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()
    exames = serializers.SerializerMethodField()

    def get_exames(self, instance):
        lst_qset = []
        if instance.id is not None:
            qset = instance.exames.get_queryset()
            for item in qset:
                d = dict(id = item.id, exame = item.exame.descricao, valor = item.valor_exame )
                lst_qset.append(d)
        return lst_qset


    class Meta:
        model = Consulta
        fields = ('numero_guia_consulta', 'cod_medico', 'nome_medico', 'data_consulta',
                  'valor_consulta', 'exames', 'links')

    def get_links(self, obj):
        request = self.context['request']
        links = {'self': reverse('consulta-detail', kwargs={'pk': obj.pk}, request=request)}

        if bool(request.POST):
            pass
        return links

class LogdbSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Logdb
        fields = ('post_req','post_curl','links')

    def get_links(self, obj):
        request = self.context['request']
        links = {'self': reverse('logdb-detail', kwargs={'pk': obj.pk}, request=request)}

        if bool(request.POST):
            pass
        return links


class TrackSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = APIRequestLog
        fields = ('user', 'requested_at', 'path', 'remote_addr', 'host', 'method', 'query_params',
                  'data', 'response', 'status_code', 'links',
                 )

        read_only_fields = fields

    def get_links(self, obj):
        request = self.context['request']
        links = {'self': reverse('apirequestlog-detail', kwargs={'pk': obj.pk}, request=request)}

        if bool(request.POST):
            pass
        return links


# TODO API para exames realizados
'''
class ExameSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = ExameRealizado
        fields = ('consulta', 'valor_exame', 'links')

    def get_links(self, obj):
        request = self.context['request']
        links = {'self': reverse('consulta-detail', kwargs={'pk': obj.pk}, request=request)}

        if bool(request.POST):
            pass
        return links
'''
